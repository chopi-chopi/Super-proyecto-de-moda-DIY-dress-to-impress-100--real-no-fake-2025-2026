import os
import pygame

pygame.font.init()

screen = pygame.display.set_mode((1200,600))
# Colores y fuente
PINK = (255, 192, 203)
LIGHT_GREEN = (144, 238, 144)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)

# intentar cargar la fuente Daydream desde assets; usar fallback si no está
font_path = os.path.normpath(os.path.join(
	os.path.dirname(__file__), '..', '..', 'assets', 'daydream_3', 'Daydream DEMO.otf'
))
try:
	font = pygame.font.Font(font_path, 29)
except Exception:
	font = pygame.font.SysFont(None, 29)

def guardar_partida(self, data, juego_nuevo):
    import pantalla_principal
    self._data = data
    self._juego_nuevo = juego_nuevo
    partidas = []
    
    if self._juego_nuevo not in partidas:
        partidas.append(self._juego_nuevo)

class BOTONES():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		base_color = WHITE
		hovering_color = GREY
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)











