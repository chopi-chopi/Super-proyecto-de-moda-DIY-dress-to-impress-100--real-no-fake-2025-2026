import os
import pygame

pygame.font.init()

screen = pygame.display.set_mode((1200,600))
# Colores y fuente
PINK = (255, 192, 203)
LIGHT_GREEN = (144, 238, 144)
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Arial', 48)

import os, pygame
screen = pygame.display.set_mode((1280,600))

def guardar_partida(self, data, juego_nuevo):
    self._data = data
    self._juego_nuevo = juego_nuevo
    partidas = []
    
    if self._juego_nuevo not in partidas:
        partidas.append(self._juego_nuevo)












