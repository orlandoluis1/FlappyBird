import pygame
from settings import WIDTH, HEIGHT

pygame.font.init()

class GameIndicator:
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont('Bauhaus 93', 60)
		self.inst_font = pygame.font.SysFont('Bauhaus 93', 30)

		self.score_colors = [
			pygame.Color("red"),
			pygame.Color("orange"),
			pygame.Color("yellow"),
			pygame.Color("green"),
			pygame.Color("blue"),
			pygame.Color("purple")
		]
		self.current_color_index = 0
		self.color_change_delay = 5
		self.color_counter = 0

		self.inst_color = pygame.Color("black")

		self.logo_img = pygame.image.load('assets/Flappy_Bird_logo.png').convert_alpha()
		self.logo_img = pygame.transform.scale(self.logo_img, (300, 100)) 
		self.logo_rect = self.logo_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))

	def _show_logo(self):
		self.screen.blit(self.logo_img, self.logo_rect)

	def show_score(self, int_score):
		
		self.color_counter += 1
		if self.color_counter >= self.color_change_delay:
			self.current_color_index = (self.current_color_index + 1) % len(self.score_colors)
			self.color_counter = 0
		
		current_color = self.score_colors[self.current_color_index]
		
		bird_score = str(int_score)
		score = self.font.render(bird_score, True, current_color)
		self.screen.blit(score, (WIDTH // 2, 50))

	def instructions(self):
		self._show_logo()

		inst_text1 = "Pressione Espaco para pular,"
		ins1 = self.inst_font.render(inst_text1, True, self.inst_color)
		ins1_rect = ins1.get_rect(center=(WIDTH // 2, 400))
		self.screen.blit(ins1, ins1_rect)
