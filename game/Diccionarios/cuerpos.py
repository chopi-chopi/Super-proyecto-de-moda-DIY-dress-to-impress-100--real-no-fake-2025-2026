import pygame 
import os

pygame.init()

modelos_cuerpo = {}
for carpeta_actual, subcarpetas, archivos in os.walk(os.path.join("game", "Assets", "Cuerpos")):
    for archivo in archivos:
        if archivo.endswith(".png"):
            ruta_completa = os.path.join(carpeta_actual, archivo)
            imagen = pygame.image.load(ruta_completa).convert_alpha()
            nombre_modelo = os.path.splitext(archivo)[0]
            modelos_cuerpo[nombre_modelo] = imagen