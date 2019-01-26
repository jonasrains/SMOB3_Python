import pygame

import mario

pygame.init()
display = pygame.display.set_mode((512, 480))
pygame.display.set_caption('Super Mario Odyssey Bros. 3')
pygame.display.set_icon(pygame.image.load(r'./images/icon.png'))
clock = pygame.time.Clock()
pygame.font.init()

areas = 4
running = True
camx = 0
camx_min = 256
camx_max = 256 + (areas - 1) * 512
camy = 0
camy_min = 186
camy_max = -(186 + 2 * 372)
screen = 'title'
world = 1
level = 1
right_pressed = False
left_pressed = False
up_pressed = False
area_imgs = []

border = pygame.image.load(r'./images/game elements/bottom border.png')


def load_background():
    global area_imgs
    area_imgs = []

    for area in range(areas):
        area_imgs += [pygame.image.load(r'./images/game elements/ground/world ' + str(world) + '/level ' + str(level) + '/' + str(area + 1) + '.png').convert_alpha()]


def center_camera():
    global camx, camy, camx_min, camx_max, camy_min, camy_min
    if mario.xpos < camx_min:
        camx = camx_min
    elif mario.xpos > camx_max:
        camx = camx_max
    else:
        camx = mario.xpos
    if mario.ypos > camy_min:
        camy = camy_min
    elif mario.ypos < camy_max:
        camy = camy_max
    else:
        camy = mario.ypos


mario.enter_level(world, level)
load_background()

while running:
    display.fill((182, 229, 235))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RIGHT:
                right_pressed = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
            if event.key == pygame.K_UP:
                up_pressed = True
            #if event.key == pygame.K_SPACE:
            #    mario.ypos = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_UP:
                up_pressed = False
        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            print(str(-(-mouse_position[0] - camx + 256)) + ', ' + str(-(-mouse_position[1] - camy + 186)))

    mario.update(left_pressed, right_pressed, up_pressed, level, world)
    center_camera()

    for area in range(areas):
        image = area_imgs[area]
        display.blit(image, ((area * 512)-camx + 256, -camy + 186))
    if mario.direction == 90:
        display.blit(mario.image, (mario.xpos - camx + 256, mario.ypos - camy + 186))
    else:
        display.blit(pygame.transform.flip(mario.image, True, False), (mario.xpos - camx + 256, mario.ypos - camy + 186))
    display.blit(border, (0, 0))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
