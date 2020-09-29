import pygame
import math
import collision
import json
import cappy

json_data = open('hitboxes.json').read()
hitboxes = json.loads(json_data)
print(hitboxes)

direction = 90
ground_hitbox = []
xpos = 0
ypos = 0
yoffset = 0
frame = 1
running = False
walk_anim = 1
max_speed = 3
velocity = 0
image = pygame.image.load(r'./images/game elements/mario/1.png')
images = []
jumping = False
jump_rep = 0
jump_height = 20
up_released = False
falling = False
crouching = False
world = 0
level = 0


def load_images():
    global images
    for i in range(54):
        images += [pygame.image.load(r'./images/game elements/mario/' + str(i+1) + '.png').convert_alpha()]


def enter_level(w, l):
    global running, xpos, ypos, ground_hitbox, world, level
    world = w
    level = l
    load_images()
    cappy.load_images()
    running = True
    ground_hitbox = hitboxes['ground'][str(world) + '-' + str(level)]
    print(ground_hitbox)
    if world == 1 and level == 1:
        xpos = 16
        ypos = 0  # 280


def touch_ground():
    return collision.collision([[xpos - 16, xpos + 16], [ypos - 32, ypos + 22]], hitboxes['ground'][str(world) + '-' + str(level)])


def touch_semisolid():
    for i in hitboxes['semisolid'][str(world) + '-' + str(level)]:
        collide = collision.collision([[xpos - 16, xpos + 16], [ypos + 20, ypos + 22]], i)
        if collide[0]:
            return collide
    return [False, []]


def touch_ceiling():
    return collision.collision([[xpos - 16, xpos + 16], [ypos - 32, ypos - 30]], hitboxes['ground'][str(world) + '-' + str(level)])


def crouch(down_pressed):
    global crouching
    if down_pressed and on_ground():
        crouching = True
    elif not down_pressed:
        if on_ground():
            crouching = False


def on_ground():
    return(touch_ground()[1] or touch_semisolid()[0])


def jump(up_pressed):
    global ypos, jumping, jump_rep, jump_height, up_released
    ypos += 1
    jump_rep += 1
    if (up_pressed and not jumping) and on_ground():
        jumping = True
        jump_rep = 0
        jump_height = 20
        up_released = False
    ypos -= 1
    if jumping and jump_rep < jump_height + 3:
        if not up_pressed and not up_released:
            jump_height = jump_rep
            up_released = True
        if jump_rep < jump_height:
            for i in range(3 + round(jump_rep / 2)):
                if not touch_ceiling()[0]:
                    ypos -= 1
        else:
            if not touch_ceiling()[0]:
                ypos -= (jump_rep - jump_height - 1)
        if touch_ceiling()[0]:
            ypos += 1
            jumping = False
    else:
        jumping = False


def update(left_pressed, right_pressed, up_pressed, down_pressed):
    global image, frame, walk_anim, velocity, frame, direction, xpos, ypos, falling, yoffset
    falling = False
    crouch(down_pressed)
    while (touch_ground()[0] and 2 not in touch_ground()[1]) or (touch_semisolid()[0] and 2 not in touch_semisolid()[1]) and not jumping:
        ypos -= 1

    ypos += 1
    if not (right_pressed and left_pressed) and (not crouching or (crouching and not on_ground())):
        if right_pressed or left_pressed:
            if on_ground():
                if walk_anim > 24:
                    walk_anim = 1
                else:
                    walk_anim += 1
            else:
                falling = True
                walk_anim = 18
        else:
            if not math.ceil(walk_anim) / 6 == 1:
                if on_ground():
                    if walk_anim > 24:
                        walk_anim = 1
                    else:
                        walk_anim += 1
            if not on_ground():
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
            if on_ground():
                if walk_anim > 24:
                    walk_anim = 1
                else:
                    walk_anim += 1
        if not on_ground():
            falling = True
            walk_anim = 18
        velocity = velocity * .8
        if abs(velocity) < .02:
            velocity = 0
    ypos -= 2
    if 2 not in touch_ground()[1]:
        xpos += velocity
    if 2 in touch_ground()[1]:
        while 2 in touch_ground()[1]:
            if velocity != 0:
                xpos = xpos - (abs(velocity)/velocity)
        velocity = 0
    ypos += 1


    jump(up_pressed)

    if not jumping:
        for i in range(6):
            if not on_ground():
                ypos += 1

    if crouching:
        yoffset = 20
        frame = 5
    else:
        yoffset = 0
        if jumping:
            frame = 4
        elif falling:
            frame = 3
        elif ((velocity < 0 and right_pressed) or (velocity > 0 and left_pressed)) and not(left_pressed and right_pressed):
            frame = 6
        else:
            if math.ceil(walk_anim / 6) == 1:
                frame = 1
            elif math.ceil(walk_anim / 6) == 2 or math.ceil(walk_anim / 6) == 4:
                frame = 2
            elif math.ceil(walk_anim / 6) == 3:
                frame = 3
    image = images[frame - 1]