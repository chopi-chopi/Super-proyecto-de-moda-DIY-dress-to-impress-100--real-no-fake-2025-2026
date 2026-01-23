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
GREY = settings.GREY
font = settings.font
MENU_MOUSE_POS = pygame.mouse.get_pos()

# Loop principal de la pantalla de título
def start_screen():
    global running
    global current_screen

    base_dir = os.path.dirname(__file__)
    image_path = os.path.normpath(os.path.join(base_dir, "..", "assets", "FONDOS", "fondo principal.png"))

    foto_path = os.path.join(os.path.dirname(__file__), "..", "assets", "NOMBRES", "TITULO V.1.png")
    titulo_overlay = None
    try:
        titulo_overlay = pygame.image.load(foto_path).convert_alpha()
        titulo_overlay = pygame.transform.scale(titulo_overlay, (350, 350))
    except Exception as e:
        print(f"No se pudo cargar el título: {foto_path} -> {e}")
    TITULO_OVERLAY_RECT = titulo_overlay.get_rect(center=(605, 100)) if titulo_overlay else None


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
                 current_screen = "cargar"
                 break
                elif OPCIONES.checkForInput(event.pos):
                 current_screen = "opciones"
                 break 
    
        # Render por frame
        screen.blit(fondo, (0, 0))
        if titulo_overlay and TITULO_OVERLAY_RECT:
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
    image_path = os.path.normpath(os.path.join(base_dir, "..", "assets", "FONDOS", "Fondo-cambiador de ropa.png"))

    #imagen de cuerpo
    img_path = os.path.join(os.path.dirname(__file__), "..", "assets", "BODYS", "cuerpo#1.png")
    overlay = None
    try:
        overlay = pygame.image.load(img_path).convert_alpha()
        overlay = pygame.transform.scale(overlay, (450, 600))
    except Exception as e:
        print(f"No se pudo cargar el cuerpo: {img_path} -> {e}")
    overlay_rect = overlay.get_rect(center=(250, 295)) if overlay else None

    # Load categories
    ROPA_dir = os.path.join(base_dir, "..", "assets", "ROPA")
    categories = []
    try:
        for item in os.listdir(ROPA_dir):
            item_path = os.path.join(ROPA_dir, item)
            if os.path.isdir(item_path):
                categories.append(item)
    except Exception as e:
        print(f"Error loading categories: {e}")
    categories.sort()

    # Load items for each category
    category_items = {}
    for cat in categories:
        cat_dir = os.path.join(ROPA_dir, cat)
        items = []
        try:
            for sub in os.listdir(cat_dir):
                sub_path = os.path.join(cat_dir, sub)
                if os.path.isdir(sub_path):
                    pngs = [os.path.join(sub_path, f) for f in os.listdir(sub_path) if f.lower().endswith('.png')]
                    items.extend(pngs)
        except Exception as e:
            print(f"Error loading items for {cat}: {e}")
        category_items[cat] = items

    current_selections = {cat: -1 for cat in categories}  # -1 means none
    selected_images = {}

    # Buttons for categories
    small_font = pygame.font.Font(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets", "daydream_3", "Daydream DEMO.otf")), 20)
    buttons = []
    x = 50
    for cat in categories:
        btn = settings.BOTONES(None, (x, 50), cat, small_font, WHITE, GREY)
        buttons.append(btn)
        x += 150

    fondo = None
    try:
        fondo = pygame.image.load(image_path).convert()
        fondo = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {image_path} -> {e}")

    while running and current_screen == "nuevo_juego":
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    current_screen = "menu" 
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, btn in enumerate(buttons):
                    if btn.checkForInput(event.pos):
                        cat = categories[i]
                        items = category_items[cat]
                        if items:
                            current_selections[cat] = (current_selections[cat] + 1) % (len(items) + 1)  # +1 for none
                            if current_selections[cat] < len(items):
                                path = items[current_selections[cat]]
                                try:
                                    img = pygame.image.load(path).convert_alpha()
                                    img = pygame.transform.smoothscale(img, (450, 600))
                                    selected_images[cat] = img
                                except Exception as e:
                                    print(f"Error loading {path}: {e}")
                                    selected_images[cat] = None
                            else:
                                selected_images[cat] = None
                        break
                
        screen.blit(fondo, (0, 0))
        if overlay and overlay_rect:
            screen.blit(overlay, overlay_rect)

        for img in selected_images.values():
            if img:
                screen.blit(img, overlay_rect)

        for btn in buttons:
            btn.changeColor(PLAY_MOUSE_POS)
            btn.update(screen)

        pygame.display.flip()

def cargar_juego():
    while running and current_screen == "cargar_juego":
        LOAD_MOUSE_POS = pygame.mouse.get_pos()

        pygame.display.flip()

def opciones():
    while running and current_screen == "opciones":
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("lightblue")
        screen.blit(font.render("opciones", True, WHITE), (500,300))

        pygame.display.flip()

if __name__ == '__main__':
    while running:
        try:
            if current_screen == 'menu':
                start_screen()
            elif current_screen == 'nuevo_juego':
                nuevo_juego()
            elif current_screen == 'cargar':
                cargar_juego()
            elif current_screen == 'opciones':
                opciones()
        except Exception as e:
            print(f"Error in main loop: {e}")
            running = False