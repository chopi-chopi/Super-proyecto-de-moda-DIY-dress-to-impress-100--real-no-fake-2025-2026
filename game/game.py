#codigo principal¿
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False


    screen.fill("pink")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()