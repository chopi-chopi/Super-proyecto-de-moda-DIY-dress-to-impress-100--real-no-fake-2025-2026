## pruebita del modelo, PREGUNTAR!!!!
"""Modelo base: sprite con carga segura de imagen desde la carpeta assets.

Para usar una imagen desde tu PC, copia el archivo (por ejemplo: modelo_base.png)
en esta carpeta: game.py/assets/ . A continuación la clase intentará cargarla.
"""

import os
import pygame

class ModeloBase(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Construye el path relativo a este archivo para que funcione desde cualquier cwd
        base_dir = os.path.dirname(__file__)
        image_name = f"body_img.png"
        image_path = os.path.join(base_dir, "assets", image_name)

        # Cargar la imagen de forma segura: convert_alpha preserva transparencia (png)
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except FileNotFoundError:
            # Si no existe, crea una superficie de marcador (visual) para evitar excepción
            print(f"[WARNING] Imagen no encontrada: {image_path}")
            self.image = pygame.Surface((50, 50))
            self.image.fill((200, 200, 200))

        self.rect = self.image.get_rect()