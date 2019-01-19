import pygame

pygame.init()
gamedisplay = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Super Mario Odyssey Bros. 3')
pygame.display.set_icon(pygame.image.load(r'./images/icon.png'))

running = True

while running:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
w
    pygame.display.update()

pygame.quit()