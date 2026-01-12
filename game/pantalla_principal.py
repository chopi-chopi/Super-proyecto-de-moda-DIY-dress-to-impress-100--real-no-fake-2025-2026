3# pantalla principal
import pygame
import settings

pygame.init(settings)
running = True
screen = settings.screen

# Colores y fuente
PINK = settings.PINK
LIGHT_GREEN = settings.LIGHT_GREEN
WHITE = settings.WHITE
font = settings.font

#definir boton(cualquier boton sera de este tamaño hasta que se diga lo contrario)
button_rect = pygame.Rect(435, 200, 400, 100)

def draw_button(surface, rect, text, mouse_pos): # dibuja boton con texto

    pygame.draw.rect(surface, PINK, rect)
    pygame.draw.rect(surface, LIGHT_GREEN, rect, 3)  # borde

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# Loop principal de la pantalla de título
def start_screen():
 while running == True:
  while running:
    screen.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()

    title_screen = font.render("KISS KISS FALL IN LOVE", True, PINK)

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
