import pygame

pygame.init()
screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Super Mario Odyssey Bros. 3')
pygame.display.set_icon(pygame.image.load(r'./images/icon.png'))
clock = pygame.time.Clock()

running = True

while running:
    screen.fill((182, 229, 235))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()