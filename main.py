import pygame
import mario


pygame.init()
display = pygame.display.set_mode((512, 480))
pygame.display.set_caption('Super Mario Odyssey Bros. 3')
pygame.display.set_icon(pygame.image.load(r'./images/icon.png'))
clock = pygame.time.Clock()

running = True
screen = 'title'
world = 1
level = 1


def update_mario():
    mario.update()


mario.enter_level(world, level)

while running:
    update_mario()
    display.fill((182, 229, 235))
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if mario.direction == 90:
        display.blit(mario.image, (mario.xpos, mario.ypos))
    else:
        display.blit(pygame.transform.flip(mario.image, True, False), (mario.xpos, mario.ypos))
    pygame.display.update()
    clock.tick(60)
pygame.quit()