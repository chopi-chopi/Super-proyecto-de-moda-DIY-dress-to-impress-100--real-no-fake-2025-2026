import pygame
import os

pygame.init()
current_screen = "menu"
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
    global running
    global current_screen

    base_dir = os.path.dirname(__file__)
    image_path = os.path.normpath(os.path.join(base_dir, "..", "assets", "FONDOS", "fondo principal.png"))

    foto_path = os.path.join(os.path.dirname(__file__), "..", "assets", "NOMBRES", "TITULO V.1.png")
    titulo_overlay = pygame.image.load(foto_path).convert_alpha()
    titulo_overlay = pygame.transform.scale(titulo_overlay, (350, 350))
    TITULO_OVERLAY_RECT = titulo_overlay.get_rect(center=(605, 100))


    fondo = None
    try:
        fondo = pygame.image.load(image_path).convert()
        fondo = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {image_path} -> {e}")
    
    NUEVO_JUEGO = settings.BOTONES(None, (605, 240), "NUEVO JUEGO", font, PINK, LIGHT_GREEN)
    CARGAR_JUEGO = settings.BOTONES(None, (605, 325), "CARGAR JUEGO", font, PINK, LIGHT_GREEN)
    OPCIONES = settings.BOTONES(None, (605, 420), "OPCIONES", font, PINK, LIGHT_GREEN)
    
    while running and current_screen == "menu":
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if NUEVO_JUEGO.checkForInput(event.pos):
                 current_screen = "nuevo_juego"
                 break
                elif CARGAR_JUEGO.checkForInput(event.pos):
                 current_screen = "cargar_juego"
                 break
                elif OPCIONES.checkForInput(event.pos):
                 current_screen = "opciones"
                 break 
    
        # Render por frame
        screen.blit(fondo, (0, 0))
        screen.blit(titulo_overlay, TITULO_OVERLAY_RECT)

        

        NUEVO_JUEGO.changeColor(MENU_MOUSE_POS)
        NUEVO_JUEGO.update(screen)
        CARGAR_JUEGO.changeColor(MENU_MOUSE_POS)
        CARGAR_JUEGO.update(screen)
        OPCIONES.changeColor(MENU_MOUSE_POS)
        OPCIONES.update(screen)

        pygame.display.flip()

def nuevo_juego():
    global running
    global current_screen
    
    #fondo de pantalla
    base_dir = os.path.dirname(__file__)
    image_path = os.path.normpath(os.path.join(base_dir, "..", "assets", "FONDOS", "fondo-cambiador de ropa.png"))

    #imagen de cuerpo
    img_path = os.path.join(os.path.dirname(__file__), "..", "assets", "BODYS", "cuerpo#1.png")
    overlay = pygame.image.load(img_path).convert_alpha()
    overlay = pygame.transform.scale(overlay, (450, 600))
    overlay_rect = overlay.get_rect(center=(250, 295))

    #imagen de ropa-N cantidad de ropa
    N = "TORSO"
    N_dir = os.path.join(base_dir, "..", "assets", "ROPA", N)
    cloth_path =[]
    try:
        for archivo in os.listdir(N_dir):
            if archivo.lower().endswith(".png"):
                cloth_path.append(os.path.join(N_dir, archivo))
    except Exception as e:
        cloth_path = []

    cloth_path.sort()  # Ordenar las rutas de las imágenes para consistencia
    max_botones = 6
    cloth_path= cloth_path[:max_botones]

    #miniatura de la ropa
    
    thumb_rects =[]
    posi_w, posi_h = 150, 150
    gap =40
    start_x= 590
    start_y= 150
    for fila in range(2):
        for columna in range (3):
            x = start_x + columna * (posi_w + gap)
            y = start_y + fila * (posi_h + gap)
            rect = pygame.Rect(x, y, posi_w, posi_h)
            thumb_rects.append(rect)

    thumbs = []
    for path in cloth_path:
        surf = pygame.image.load(path).convert_alpha()
        thumb = pygame.transform.scale(surf, (posi_w, posi_h))
        thumbs.append(thumb)

    

    fondo = None
    try:
        fondo = pygame.image.load(image_path).convert()
        fondo = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {image_path} -> {e}")



    selection_cloth = None
    selection_cloth_rect = overlay_rect.copy()


    while running and current_screen == "nuevo_juego":
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    current_screen = "menu" 
                    break
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                for idx, rect in enumerate(thumb_rects):
                    if rect.collidepoint(event.pos) and idx < len(cloth_path):
                        path = cloth_path[idx]
                        print("Cargando:", path)

                        try:
                            selection_cloth = pygame.image.load(path).convert_alpha()
                            selection_cloth = pygame.transform.scale(selection_cloth, (450, 600))
                            selection_cloth_rect = overlay_rect
                        except Exception as e:
                            print(f"No se pudo cargar la imagen de ropa: {path} -> {e}")

                
        screen.blit(fondo, (0, 0))
        screen.blit(overlay, overlay_rect)
       
        for i, rect in enumerate(thumb_rects):
                    if i < len(thumbs):
                        screen.blit(thumbs[i], rect)
                    pygame.draw.rect(screen, (0, 0, 0), rect, 2)

 
        if selection_cloth and selection_cloth_rect:
            screen.blit(selection_cloth, selection_cloth_rect)
        
        pygame.display.flip()

    
        
       


    fondo = None
    try:
        fondo = pygame.image.load(image_path).convert()
        fondo = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {image_path} -> {e}")

        pygame.display.flip()
       
        
def cargar_juego():
    while running and current_screen == "cargar_juego":
        LOAD_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("lightblue")
        screen.blit(font.render("cargar juego", True, WHITE), (500,300))
        pygame.display.flip()

def opciones():
    while running and current_screen == "opciones":
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("lightblue")
        screen.blit(font.render("opciones", True, WHITE), (500,300))

        pygame.display.flip()

if __name__ == '__main__':
    while running:
        if current_screen == 'menu':
            start_screen()
        elif current_screen == 'nuevo_juego':
            nuevo_juego()
        elif current_screen == 'cargar':
            cargar_juego()
        elif current_screen == 'opciones':
            opciones()