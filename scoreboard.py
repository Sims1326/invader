import pygame
from stats import Stats


class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.width, self.height = 200, 50
        self.text_color = (30, 30, 30)

        self.text_font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):

        score_str = str(self.stats.points)

        self.score_img = self.text_font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        self.score_img_rect = self.score_img.get_rect()

        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_img_rect)
