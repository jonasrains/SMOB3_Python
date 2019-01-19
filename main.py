import pygame

pygame.init()

gamedisplay = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Super Mario Odyssey Bros. 3')
a = pygame.image.load(r'./images/temp.png')
pygame.display.set_icon(a)
while True:

    for event in pygame.event.get():
        print(event)
    pygame.display.update()

pygame.quit()