import pygame

direction = 90
xpos = 0
ypos = 0
frame = 1
running = False
image = pygame.image.load(r'./images/game elements/mario/' + str(frame) + '.png')


def enter_level(world, level):
    global running, xpos, ypos
    running = True
    if world == 1 and level == 1:
        xpos = 0
        ypos = 0


def update():
    global image
    image = pygame.image.load(r'./images/game elements/mario/' + str(frame) + '.png')
