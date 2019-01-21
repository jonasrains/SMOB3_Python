import pygame
import math

import collision
import json

json_data = open('hitboxes.json').read()

data = json.loads(json_data)
print(data)

direction = 90
ground_hitbox = []
xpos = 0
ypos = 0
frame = 1
running = False
walk_anim = 1
max_speed = 3
velocity = 0
image = pygame.image.load(r'./images/game elements/mario/' + str(frame) + '.png')
images = []


def load_images():
    global images
    for i in range(54):
        images += [pygame.image.load(r'./images/game elements/mario/' + str(i+1) + '.png').convert_alpha()]


def enter_level(world, level):
    global running, xpos, ypos, ground_hitbox
    load_images()
    running = True
    ground_hitbox = data['ground'][str(world) + '-' + str(level)]
    print(ground_hitbox)
    if world == 1 and level == 1:
        xpos = 0
        ypos = 0  # 280


def touch_ground(world, level):
    return collision.collision([[xpos, xpos + 28], [ypos, ypos + 54]], data['ground'][str(world) + '-' + str(level)])


def update(left_pressed, right_pressed, level, world):
    global image, frame, walk_anim, velocity, frame, direction, xpos, ypos
    while touch_ground(world, level)[0] and 2 not in touch_ground(world, level)[1]:
        ypos -= 1

    ypos += 1
    if not (right_pressed and left_pressed):
        if right_pressed or left_pressed:
            if touch_ground(world, level)[0]:
                if walk_anim > 24:
                    walk_anim = 1
                else:
                    walk_anim += 1
            else:
                walk_anim = 18
        else:
            if not math.ceil(walk_anim) / 6 == 1:
                if touch_ground(world, level)[0]:
                    if walk_anim > 24:
                        walk_anim = 1
                    else:
                        walk_anim += 1
                else:
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
            if touch_ground(world, level)[0]:
                if walk_anim > 24:
                    walk_anim = 1
                else:
                    walk_anim += 1
            else:
                walk_anim = 18
        velocity = velocity * .8
        if abs(velocity) < .02:
            velocity = 0
    ypos -= 2
    if 2 not in touch_ground(world, level)[1]:
        xpos += velocity
    if 2 in touch_ground(world, level)[1]:
        while 2 in touch_ground(world, level)[1]:
            if velocity != 0:
                xpos = xpos - (abs(velocity)/velocity)
        velocity = 0
    ypos += 1

    for i in range(7):
        if not touch_ground(world, level)[0]:
            ypos += 1

    if ((velocity < 0 and right_pressed) or (velocity > 0 and left_pressed)) and not(left_pressed and right_pressed):
        frame = 6
    else:
        if math.ceil(walk_anim) / 6 == 1:
            frame = 1
        elif math.ceil(walk_anim) / 6 == 2 or math.ceil(walk_anim) / 6 == 4:
            frame = 2
        elif math.ceil(walk_anim) / 6 == 3:
            frame = 3
    image = images[frame - 1]
