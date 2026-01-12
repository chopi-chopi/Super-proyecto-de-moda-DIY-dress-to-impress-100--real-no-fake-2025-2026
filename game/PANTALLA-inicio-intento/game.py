#codigo principal¿
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,600))
running = True


fondo_img=pygame.image.load("pancarga").convert()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

    screen.blit(fondo_img, (0, 0))
    
    pygame.display.flip()
#mi foking intento todo piedrero


pygame.quit()