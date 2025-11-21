# pantalla principal
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,600))
running = True

PINK = (255, 192, 203)
LIGHT_GREEN = (144, 238, 144)
WHITE = (255, 255, 255)
font = pygame.font.SysFont("IBM 3270",74)
button_rect = pygame.Rect(540, 200, 200, 100)

def draw_button(surface, rect, text, mouse_pos):

    pygame.draw.rect(surface, PINK, rect)
    pygame.draw.rect(surface, LIGHT_GREEN, rect, 3)  # borde

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

running = True
while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()

    # Dibujar botón
    draw_button(screen, button_rect, "Nuevo juego", mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("¡Botón de inicio presionado!")
                # Aquí puedes cambiar de pantalla o iniciar el juego

    pygame.display.flip() #esto hace que la cosa salga en pantalla, NO MOVER!!!!

pygame.quit()
