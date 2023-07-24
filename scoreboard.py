import pygame
from player_character import Player
from pygame.sprite import Group


class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.game = game

        self.width, self.height = 200, 50
        self.text_color = (30, 30, 30)

        self.text_font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_lives()
        self.prep_level()

    def prep_level(self):

        level_str = f" Level: {str(self.settings.level)}"

        self.level_img = self.text_font.render(
            level_str, True, self.text_color, self.settings.bg_color)
        self.level_img_rect = self.level_img.get_rect()

        self.level_img_rect.right = self.screen_rect.right - 20
        self.level_img_rect.bottom = 800

    def prep_score(self):

        score_str = str(self.stats.points)

        self.score_img = self.text_font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        self.score_img_rect = self.score_img.get_rect()

        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20

    def prep_lives(self):

        self.lives = Group()

        for lives in range(self.settings.lives):
            life = Player(self.game)
            life.rect.x = 10 + lives * life.rect.width
            life.rect.y = 10
            self.lives.add(life)

    def check_hs(self):
        if self.stats.points > self.stats.high_score:
            self.stats.high_score = self.stats.points
            self.prep_high_score()

    def prep_high_score(self):

        high_score_str = "{:,}".format(self.stats.high_score)

        self.high_score_img = self.text_font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def show_score(self):
        self.screen.blit(self.score_img, self.score_img_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_img_rect)
        self.lives.draw(self.screen)
