# pantalla principal
import os
import importlib.util
import pygame
from game import nuevo_juego, cargar_juego, opciones

pygame.init()
from settings import settings
running = True
screen = settings.screen

# Colores y fuente
PINK = settings.PINK
LIGHT_GREEN = settings.LIGHT_GREEN
WHITE = settings.WHITE
font = settings.font
MENU_MOUSE_POS = pygame.mouse.get_pos()

#definir boton(cualquier boton sera de este tamaño hasta que se diga lo contrario)
NUEVO_JUEGO = pygame.Rect(435, 200, 400, 100) #los primeros dos son anchoxaltura, los otros son de posicion
small_button_rect = pygame.Rect(220, 100, 200, 50)

def draw_button(surface, rect, text, mouse_pos): # dibuja boton con texto

    pygame.draw.rect(surface, PINK, rect)
    pygame.draw.rect(surface, LIGHT_GREEN, rect, 3)  # borde

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# Loop principal de la pantalla de título
def start_screen():
    running = True
    CARGAR_JUEGO = pygame.Rect(435, 320, 200, 50)  
    OPCIONES = pygame.Rect(635, 320, 200, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if NUEVO_JUEGO.collidepoint(event.pos):
                    nuevo_juego()
                elif CARGAR_JUEGO.collidepoint(event.pos):
                    cargar_juego()
                elif OPCIONES.collidepoint(event.pos):
                    opciones()

        # Render por frame
        screen.fill(WHITE)

        # Render del título
        title_screen = font.render("KISS KISS FALL IN LOVE", True, PINK)
        title_rect = title_screen.get_rect(center=(screen.get_width() // 2, 80))
        screen.blit(title_screen, title_rect)

        # Dibujar botones
        draw_button(screen, NUEVO_JUEGO, "Nuevo juego", MENU_MOUSE_POS)
        draw_button(screen, CARGAR_JUEGO, "Cargar juego", MENU_MOUSE_POS)
        draw_button(screen, OPCIONES, "Opciones", MENU_MOUSE_POS)

        pygame.display.flip()



if __name__ == '__main__':
    start_screen()
    pygame.quit()