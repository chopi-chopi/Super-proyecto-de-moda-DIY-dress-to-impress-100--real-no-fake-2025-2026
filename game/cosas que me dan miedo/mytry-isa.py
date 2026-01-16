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
    
    NUEVO_JUEGO = settings.BOTONES(None, (640, 250), "NUEVO JUEGO", font, PINK, LIGHT_GREEN)
    CARGAR_JUEGO = settings.BOTONES(None, (640, 320), "CARGAR JUEGO", font, PINK, LIGHT_GREEN)
    OPCIONES = settings.BOTONES(None, (640, 390), "OPCIONES", font, PINK, LIGHT_GREEN)
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
            

            screen.blit(fondo, (0, 0))
            screen.blit(overlay, overlay_rect)
            pygame.display.flip()

    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = "menu"
                    break

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