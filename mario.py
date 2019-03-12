import pygame
import math

import collision
import json

json_data = open('hitboxes.json').read()

data = json.loads(json_data)
print(data)

direction = 90
ground_hit_box = []
x_pos = 0
y_pos = 0
frame = 1
running = False
walk_anim = 1
max_speed = 3
velocity = 0
image = pygame.image.load(r'./images/game elements/mario/' + str(frame) + '.png')
images = []
jumping = False
jump_rep = 0
jump_height = 20
up_released = False
falling = False


def load_images():
    global images
    for i in range(54):
        images += [pygame.image.load(r'./images/game elements/mario/' + str(i+1) + '.png').convert_alpha()]


def enter_level(world, level):
    global running, x_pos, y_pos, ground_hit_box
    load_images()
    running = True
    ground_hit_box = data['ground'][str(world) + '-' + str(level)]
    print(ground_hit_box)
    if world == 1 and level == 1:
        x_pos = 0
        y_pos = 0  # 280


def touch_ground(world, level):
    return collision.collision([[x_pos, x_pos + 28], [y_pos, y_pos + 54]], data['ground'][str(world) + '-' + str(level)])


def touch_semisolid(world, level):
    for i in data['semisolid'][str(world) + '-' + str(level)]:
        collide = collision.collision([[x_pos, x_pos + 28], [y_pos + 52, y_pos + 54]], i)
        if collide[0]:
            return collide
    return [False, []]


def touch_ceiling(world, level):
    return collision.collision([[x_pos, x_pos + 28], [y_pos, y_pos + 2]], data['ground'][str(world) + '-' + str(level)])


def jump(up_pressed, world, level):
    global y_pos, jumping, jump_rep, jump_height, up_released
    y_pos += 1
    if (up_pressed and not jumping) and (touch_ground(world, level)[1] or touch_semisolid(world, level)[0]):
        jumping = True
        jump_rep = 0
        jump_height = 20
        up_released = False
    y_pos -= 1
    if jumping and jump_rep < jump_height + 2:
        jump_rep += 1
        if not up_pressed and not up_released:
            jump_height = jump_rep + 2
            up_released = True
        if jump_rep < jump_height:
            for i in range(3 + round(jump_rep / 2)):
                if not touch_ceiling(world, level)[0]:
                    y_pos -= 1
        else:
            for i in range(round(abs((jump_rep - jump_height)/2))):
                if not touch_ceiling(world, level)[0]:
                    y_pos -= ((0-(abs(jump_rep - jump_height) / (jump_rep - jump_height)))*4)
        if touch_ceiling(world, level)[0]:
            y_pos += 1
            jumping = False
    else:
        jumping = False



def update(left_pressed, right_pressed, up_pressed, level, world):
    global image, frame, walk_anim, velocity, frame, direction, x_pos, y_pos, falling
    falling = False
    while (touch_ground(world, level)[0] and 2 not in touch_ground(world, level)[1]) or (touch_semisolid(world, level)[0] and 2 not in touch_semisolid(world, level)[1]) and not jumping:
        y_pos -= 1

    y_pos += 1
    if not (right_pressed and left_pressed):
        if right_pressed or left_pressed:
            if touch_ground(world, level)[0] or touch_semisolid(world, level)[0]:
                if walk_anim > 24:
                    walk_anim = 1
                else:
                    walk_anim += 1
            else:
                falling = True
                walk_anim = 18
        else:
            if not math.ceil(walk_anim) / 6 == 1:
                if touch_ground(world, level)[0] or touch_semisolid(world, level)[0]:
                    if walk_anim > 24:
                        walk_anim = 1
                    else:
                        walk_anim += 1
            if not (touch_ground(world, level)[0] or touch_semisolid(world, level)[0]):
                falling = True
                walk_anim = 18
        if right_pressed:
            direction = 90
            if velocity < max_speed:
                velocity += .2
            else:
                velocity = max_speed
        elif left_pressed:
            direction = -90
            if velocity > - max_speed:
                velocity -= .2
            else:
                velocity = - max_speed
        else:
            velocity = velocity * .8
    else:
        if not math.ceil(walk_anim) / 6 == 1:
            if touch_ground(world, level)[0] or touch_semisolid(world, level)[0]:
                if walk_anim > 24:
                    walk_anim = 1
                else:
                    walk_anim += 1
        if not (touch_ground(world, level)[0] or touch_semisolid(world, level)[0]):
            falling = True
            walk_anim = 18
        velocity = velocity * .8
        if abs(velocity) < .02:
            velocity = 0
    y_pos -= 2
    if 2 not in touch_ground(world, level)[1]:
        x_pos += velocity
    if 2 in touch_ground(world, level)[1]:
        while 2 in touch_ground(world, level)[1]:
            if velocity != 0:
                x_pos = x_pos - (abs(velocity)/velocity)
        velocity = 0
    y_pos += 1

    jump(up_pressed, world, level)

    if not jumping:
        for i in range(6):
            if not (touch_ground(world, level)[0] or touch_semisolid(world, level)[0]):
                y_pos += 1
    if jumping:
        frame = 4
    elif falling:
        frame = 3
    elif ((velocity < 0 and right_pressed) or (velocity > 0 and left_pressed)) and not(left_pressed and right_pressed):
        frame = 6
    else:
        if math.ceil(walk_anim) / 6 == 1:
            frame = 1
        elif math.ceil(walk_anim) / 6 == 2 or math.ceil(walk_anim) / 6 == 4:
            frame = 2
        elif math.ceil(walk_anim) / 6 == 3:
            frame = 3
    image = images[frame - 1]
