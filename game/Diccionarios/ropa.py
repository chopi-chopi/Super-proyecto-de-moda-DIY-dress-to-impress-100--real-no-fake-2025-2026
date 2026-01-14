import pygame 
import os 

pygame.init() 

categorias = ["ACCESORIOS","TORSO",'PIERNAS',"ZAPATOS"]
ropa = {}

for categoria in categorias:
    ropa[categoria] = []
    ruta_carpeta = os.path.join("game", "Assets", "Ropa", categoria)
    for archivo in os.listdir(ruta_carpeta):
        if archivo.endswith(".png"):
            ruta_completa = os.path.join(ruta_carpeta, archivo)
            imagen = pygame.image.load(ruta_completa).convert_alpha()
            ropa[categoria].append(imagen)
            
              

#lowkey como se cargan los archivos
# imagen = ropa["TORSO"][0]
#screen.blit(imagen, (x, y))