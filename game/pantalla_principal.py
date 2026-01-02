# pantalla principal
import os
import importlib.util
import pygame

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

# Loop principal de la pantalla de título
def start_screen():
    running = True
    NUEVO_JUEGO = settings.BOTONES(None, (640, 250), "NUEVO JUEGO", font, PINK, LIGHT_GREEN)
    CARGAR_JUEGO = settings.BOTONES(None, (640, 320), "CARGAR JUEGO", font, PINK, LIGHT_GREEN)
    OPCIONES = settings.BOTONES(None, (640, 390), "OPCIONES", font, PINK, LIGHT_GREEN)
    while running:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if NUEVO_JUEGO.checkForInput(event.pos):
                 nuevo_juego()
                elif CARGAR_JUEGO.checkForInput(event.pos):
                 cargar_juego()
                elif OPCIONES.checkForInput(event.pos):
                 opciones()
    
        # Render por frame
        screen.fill(LIGHT_GREEN)

        # Render del título
        title_screen = font.render("KISS KISS FALL IN LOVE", True, PINK)
        title_rect = title_screen.get_rect(center=(screen.get_width() // 2, 80))
        screen.blit(title_screen, title_rect)

        NUEVO_JUEGO.changeColor(MENU_MOUSE_POS)
        NUEVO_JUEGO.update(screen)
        CARGAR_JUEGO.changeColor(MENU_MOUSE_POS)
        CARGAR_JUEGO.update(screen)
        OPCIONES.changeColor(MENU_MOUSE_POS)
        OPCIONES.update(screen)

        pygame.display.flip()

def nuevo_juego():
    while True:
     PLAY_MOUSE_POS = pygame.mouse.get_pos()
     screen.fill("pink")
     screen.blit(font.render("prueba jiji", True, WHITE), (400,300))

def cargar_juego():
    while True:
       LOAD_MOUSE_POS = pygame.mouse.get_pos()

def opciones():
    while True: 
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("lightblue")
        screen.blit(font.render("opciones", True, WHITE), (500,300))


if __name__ == '__main__':
    current_screen = "inicio"
    while True:
     if current_screen == 'menu':
            current_screen = start_screen()
     elif current_screen == 'nuevo_juego':
            current_screen = nuevo_juego()
     elif current_screen == 'cargar':
            current_screen = cargar_juego()
     elif current_screen == 'opciones':
            current_screen = opciones()