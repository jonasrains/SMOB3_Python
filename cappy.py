import pygame
import collision
import json

json_data = open('hitboxes.json').read()
hitboxes = json.loads(json_data)
print(hitboxes)

image = pygame.image.load(r'./images/game elements/cappy/1.png')
images = {'mario':[], 'luigi':[]}
thrown = False


def load_images():
    global images
    for i in range(8):
        images['mario'] += [pygame.image.load(r'./images/game elements/mario/' + str(i+1) + '.png').convert_alpha()]



def throw(player='mario'):
    global thrown
    if thrown:
        print('')


def update(player='mario'):
    global thrown
