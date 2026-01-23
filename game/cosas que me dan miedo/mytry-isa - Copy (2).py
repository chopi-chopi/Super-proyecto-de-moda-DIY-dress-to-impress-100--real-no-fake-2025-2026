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

    # Load body images
    bodys_dir = os.path.join(base_dir, "..", "assets", "BODYS")
    body_paths = []
    try:
        for f in os.listdir(bodys_dir):
            if f.lower().endswith('.png'):
                body_paths.append(os.path.join(bodys_dir, f))
    except Exception as e:
        print(f"Error loading bodies: {e}")
    body_paths.sort()
    current_body = 0

    # Load initial body
    overlay = None
    overlay_rect = None
    if body_paths:
        try:
            overlay = pygame.image.load(body_paths[current_body]).convert_alpha()
            overlay = pygame.transform.scale(overlay, (450, 600))
            overlay_rect = overlay.get_rect(center=(250, 295))
        except Exception as e:
            print(f"No se pudo cargar el cuerpo: {body_paths[current_body]} -> {e}")

    # Button for changing body
    small_font = pygame.font.Font(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets", "daydream_3", "Daydream DEMO.otf")), 20)
    change_body_img = None
    try:
        change_body_img = pygame.image.load(os.path.join(base_dir, "..", "assets", "BOTONES-interactivos", "skintone_boton.png")).convert_alpha()
        change_body_img = pygame.transform.smoothscale(change_body_img, (40, 40))
    except Exception as e:
        print(f"Error loading change body button image: {e}")
    change_body_button = settings.BOTONES(change_body_img, (497, 210), "", small_font, WHITE, GREY)

    #imagen de ropa-N cantidad de ropa
    N = "TORSO"
    N_dir = os.path.join(base_dir, "..", "assets", "ROPA", N)
    subdirs = []
    try:
        for item in os.listdir(N_dir):
            item_path = os.path.join(N_dir, item)
            if os.path.isdir(item_path):
                subdirs.append(item)
    except Exception as e:
        subdirs = []

    subdirs.sort()  # Ordenar las subcarpetas para consistencia
    per_page = 6
    current_page = 0
    total_pages = (len(subdirs) + per_page - 1) // per_page

    # Buttons
    small_font = pygame.font.Font(os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "assets", "daydream_3", "Daydream DEMO.otf")), 20)
    prev_button = settings.BOTONES(None, (770, 540), "PREV", small_font, WHITE, GREY)
    next_button = settings.BOTONES(None, (960, 540), "NEXT", small_font, WHITE, GREY)

    cloth_paths_page = []  # list of lists of paths for each subdir in page
    thumb_paths = []
    thumbs = []

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

    def load_page():
        nonlocal cloth_paths_page, thumb_paths, thumbs
        start_idx = current_page * per_page
        end_idx = start_idx + per_page
        subdirs_page = subdirs[start_idx:end_idx]
        
        cloth_paths_page = []  # list of lists of paths for each subdir in page
        thumb_paths = []
        thumbs = []
        for subdir in subdirs_page:
            subdir_path = os.path.join(N_dir, subdir)
            try:
                pngs = [f for f in os.listdir(subdir_path) if f.lower().endswith('.png')]
                pngs.sort()
                if pngs:
                    first_png = os.path.join(subdir_path, pngs[0])
                    try:
                        surf = pygame.image.load(first_png).convert_alpha()
                        thumb = pygame.transform.smoothscale(surf, (posi_w, posi_h))
                        thumbs.append(thumb)
                        thumb_paths.append(first_png)
                        cloth_paths_page.append([os.path.join(subdir_path, p) for p in pngs])
                    except Exception as e:
                        print(f"No se pudo cargar thumbnail para {subdir}: {first_png} -> {e}")
            except Exception as e:
                print(f"No se pudo listar archivos en {subdir_path}: {e}")

    load_page()  # initial load

    

    fondo = None
    try:
        fondo = pygame.image.load(image_path).convert()
        fondo = pygame.transform.scale(fondo, (screen.get_width(), screen.get_height()))
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {image_path} -> {e}")

    # Load UI buttons
    button_images = []
    button_dir = os.path.join(base_dir, "..", "assets", "BOTONES-interactivos", "BUTTONS UI")
    if os.path.exists(button_dir):
        pngs = [f for f in os.listdir(button_dir) if f.lower().endswith('.png')]
        # sort by the number before -
        def sort_key(f):
            parts = f.split('-')
            if parts and parts[0].isdigit():
                return int(parts[0])
            else:
                return 999  # put at end
        pngs.sort(key=sort_key)
        for png in pngs:
            path = os.path.join(button_dir, png)
            try:
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.smoothscale(img, (90, 90))
                button_images.append(img)
            except Exception as e:
                print(f"No se pudo cargar botón UI: {path} -> {e}")



    selection_cloth = None
    selection_cloth_rect = overlay_rect.copy() if overlay_rect else None

    selected_subdir = None
    toggle_buttons = []
    toggle_images = []


    while running and current_screen == "nuevo_juego":
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    current_screen = "menu" 
                    break
                elif event.key == pygame.K_SPACE:
                    selected_subdir = None
                    toggle_buttons = []
                    toggle_images = []
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                # Check prev/next buttons first
                if prev_button.checkForInput(event.pos) and current_page > 0:
                    current_page -= 1
                    load_page()
                    selected_subdir = None
                    toggle_buttons = []
                    toggle_images = []
                elif next_button.checkForInput(event.pos) and current_page < total_pages - 1:
                    current_page += 1
                    load_page()
                    selected_subdir = None
                    toggle_buttons = []
                    toggle_images = []
                else:
                    # Check change body button
                    if change_body_button.checkForInput(event.pos):
                        if body_paths:
                            current_body = (current_body + 1) % len(body_paths)
                            try:
                                overlay = pygame.image.load(body_paths[current_body]).convert_alpha()
                                overlay = pygame.transform.scale(overlay, (450, 600))
                                overlay_rect = overlay.get_rect(center=(250, 295))
                            except Exception as e:
                                print(f"Error loading body: {body_paths[current_body]} -> {e}")
                    else:
                        # Check thumbnails
                        thumbnail_clicked = False
                        for idx, rect in enumerate(thumb_rects):
                            if rect.collidepoint(event.pos) and idx < len(thumbs):
                                selected_subdir = idx
                                # Load toggles
                                paths = cloth_paths_page[idx][:3]  # first 3
                                toggle_images = []
                                for p in paths:
                                    try:
                                        img = pygame.image.load(p).convert_alpha()
                                        img = pygame.transform.smoothscale(img, (80, 80))
                                        toggle_images.append(img)
                                    except Exception as e:
                                        print(f"No se pudo cargar toggle: {p} -> {e}")
                                # Positions for toggles
                                toggle_buttons = []
                                tx, ty = 457, 375  # below thumbs
                                for i in range(len(toggle_images)):
                                    rect_toggle = pygame.Rect(tx, ty + i*65, 80, 80)
                                    toggle_buttons.append(rect_toggle)
                                # Reset selection
                                selection_cloth = None
                                thumbnail_clicked = True
                                break
                        # Check toggle buttons if thumbnails not clicked and selected_subdir is set
                        if not thumbnail_clicked and selected_subdir is not None:
                            for i, rect in enumerate(toggle_buttons):
                                if rect.collidepoint(event.pos) and i < len(cloth_paths_page[selected_subdir]):
                                    path = cloth_paths_page[selected_subdir][i]
                                    print("Cargando:", path)
                                    try:
                                        selection_cloth = pygame.image.load(path).convert_alpha()
                                        selection_cloth = pygame.transform.smoothscale(selection_cloth, (450, 600))
                                        selection_cloth_rect = overlay_rect
                                    except Exception as e:
                                        print(f"No se pudo cargar la imagen de ropa: {path} -> {e}")
                                    # Hide toggles after selection
                                    selected_subdir = None
                                    toggle_buttons = []
                                    toggle_images = []

                
        screen.blit(fondo, (0, 0))
        if overlay and overlay_rect:
            screen.blit(overlay, overlay_rect)

        # Draw UI buttons horizontally
        for i, img in enumerate(button_images):
            x = 545 + i * 110
            screen.blit(img, (x, 14))
       
        for i, rect in enumerate(thumb_rects):
                    if i < len(thumbs):
                        screen.blit(thumbs[i], rect)

        if selected_subdir is not None:
            for i, img in enumerate(toggle_images):
                screen.blit(img, toggle_buttons[i])

        if selection_cloth and selection_cloth_rect:
            screen.blit(selection_cloth, selection_cloth_rect)

        # Update buttons
        prev_button.changeColor(PLAY_MOUSE_POS)
        prev_button.update(screen)
        next_button.changeColor(PLAY_MOUSE_POS)
        next_button.update(screen)
        change_body_button.changeColor(PLAY_MOUSE_POS)
        change_body_button.update(screen)

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