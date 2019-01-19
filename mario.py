import pygame
import math

direction = 90
xpos = 0
ypos = 0
frame = 1
running = False
walk_anim = 1
max_speed = 3
velocity = 0
image = pygame.image.load(r'./images/game elements/mario/' + str(frame) + '.png')


def enter_level(world, level):
    global running, xpos, ypos
    running = True
    if world == 1 and level == 1:
        xpos = 0
        ypos = 0


def update(left_pressed, right_pressed):
    global image, frame, walk_anim, velocity, frame, direction, xpos, ypos

    if not (right_pressed and left_pressed):
        if right_pressed or left_pressed:
            if walk_anim > 24:
                walk_anim = 1
            else:
                walk_anim += 1
        else:
            if not 5 < walk_anim < 10:
                if walk_anim > 24:
                    walk_anim = 1
                else:
                    walk_anim += 1
        if right_pressed:
            direction = 90
            if velocity < max_speed:
                velocity += .1
            else:
                velocity = max_speed
        elif left_pressed:
            direction = -90
            if velocity > - max_speed:
                velocity -= .1
            else:
                velocity = - max_speed
        else:
            velocity = velocity * .8
    else:
        if not 5 < walk_anim < 10:
            if walk_anim > 24:
                walk_anim = 1
            else:
                walk_anim += 1
        velocity = velocity * .8
    xpos += velocity
    if ((velocity < 0 and right_pressed) or (velocity > 0 and left_pressed)) and not(left_pressed and right_pressed):
        frame = 6
    else:
        if math.ceil(walk_anim) / 6 == 1:
            frame = 1
        elif math.ceil(walk_anim) / 6 == 2 or math.ceil(walk_anim) / 6 == 4:
            frame = 2
        elif math.ceil(walk_anim) / 6 == 3:
            frame = 3
    image = pygame.image.load(r'./images/game elements/mario/' + str(frame) + '.png')
