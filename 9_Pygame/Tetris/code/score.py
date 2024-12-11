from settings import *
from os.path import join

class Score():
    def __init__(self):

        # general
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surface = pygame.display.get_surface()

        # font
        self.font = pygame.font.Font(join('..', 'assets', 'graphics', 'RussoOne-Regular.ttf'), 40)

        self.fragment_height = self.surface.get_height() / 4

        # score
        self.score = 0
        self.lines = 0


    def display_text(self, pos, text):
        text_surface = self.font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rect)
    
    def run(self, score, lines): 

        self.score = score
        self.lines = lines
        self.surface.fill(BLACK)
        for i, text in enumerate(['Score:', str(self.score), 'Lines:', str(self.lines)]):
            x = self.surface.get_width() / 2
            y = self.fragment_height * i + self.fragment_height / 2
            self.display_text((x, y), text)

        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, LIGHT_GREY, self.rect, 2, 2)