from settings import *
from sys import exit
from random import choice

# components
from game import Game
from preview import Preview
from score import Score

class Main():
	def __init__(self):

		# general
		pygame.init()
		pygame.display.set_caption('Tetris')
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.clock = pygame.time.Clock()

		# shapes
		self.next_shapes = [choice(list(TETROMINOS.keys())) for _ in range(3)]
		print(self.next_shapes)

		# components
		self.game = Game(self.get_next_shape)
		self.preview = Preview()
		self.score = Score()

		# score
		self.game_score = 0
		self.game_lines = 0

	def get_next_shape(self):
		next_shape = self.next_shapes.pop(0)
		self.next_shapes.append(choice(list(TETROMINOS.keys())))
		return next_shape

	def run(self):
		
		# game loop
		while True:

			# handle events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
			
			# display
			self.display_surface.fill(GREY)
			self.preview.run(self.next_shapes)
			self.score.run(self.game_score, self.game_lines)
			self.game_score, self.game_lines = self.game.run()

			# updating the game
			pygame.display.update()
			self.clock.tick(FPS)


if __name__ == '__main__':
	main = Main()
	main.run()

