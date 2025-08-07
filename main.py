import pygame, sys
from settings import WIDTH, HEIGHT, ground_space
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT + ground_space))
pygame.display.set_caption("Flappy Bird")

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.bg_img = pygame.image.load('assets/terrain/bg.png')
		self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))
		self.ground_img = pygame.image.load('assets/terrain/ground.png')
		self.ground_img = pygame.transform.scale(self.ground_img, (WIDTH, ground_space))

		self.ground_img_2 = self.ground_img.copy()

		self.ground_scroll_1 = 0
		self.ground_scroll_2 = WIDTH

		self.scroll_speed = -6
		self.FPS = pygame.time.Clock()
		self.stop_ground_scroll = False

	def main(self):
		world = World(screen)
		while True:
			self.stop_ground_scroll = world.game_over
			self.screen.blit(self.bg_img, (0, 0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == pygame.KEYDOWN:
					if not world.playing and not world.game_over:
						world.playing = True
					if event.key == pygame.K_SPACE:
						world.update("jump")
					if event.key == pygame.K_r:
						world.update("restart")

			world.update()

			self.screen.blit(self.ground_img, (self.ground_scroll_1, HEIGHT))
			self.screen.blit(self.ground_img_2, (self.ground_scroll_2, HEIGHT))

			if not self.stop_ground_scroll:
				self.ground_scroll_1 += self.scroll_speed
				self.ground_scroll_2 += self.scroll_speed
				
				if self.ground_scroll_1 <= -WIDTH: 
					self.ground_scroll_1 = WIDTH
				
				if self.ground_scroll_2 <= -WIDTH:
					self.ground_scroll_2 = WIDTH

			pygame.display.update()
			self.FPS.tick(60)

if __name__ == "__main__":
	play = Main(screen)
	play.main()
