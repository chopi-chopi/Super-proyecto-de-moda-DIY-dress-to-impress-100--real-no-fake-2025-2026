import os
import pygame

pygame.font.init()

screen = pygame.display.set_mode((1200,600))
# Colores y fuente
PINK = (255, 192, 203)
LIGHT_GREEN = (144, 238, 144)
WHITE = (255, 255, 255)

# Intentar cargar la fuente incluida en assets/pixel_2.ttf; si no existe, usar SysFont
font_size = 74
font = None
try:
        # Desde este archivo, subir un nivel y entrar en assets/
        base_dir = os.path.dirname(__file__)
        font_path = os.path.abspath(os.path.join(base_dir, '..', 'assets', 'pixel_2.ttf'))
        if os.path.exists(font_path):
            font = pygame.font.Font(font_path, font_size)
        else:
            # nombre dado a SysFont no garantiza que exista; usar fallback al sistema
            font = pygame.font.SysFont('pixel_2', font_size)
except Exception as e:
        print(f"Error loading font: {e}")   

import os, pygame
screen = pygame.display.set_mode((1280,600))

def guardar_partida(self, data, juego_nuevo):
    self._data = data
    self._juego_nuevo = juego_nuevo
    partidas = []
    
    if self._juego_nuevo not in partidas:
        partidas.append(self._juego_nuevo)












