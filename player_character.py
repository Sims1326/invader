import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.player_right = False
        self.player_left = False

        image = pygame.image.load('Assets/player.bmp')
        image_size = (50, 50)
        self.image = pygame.transform.scale(image, image_size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def draw_player(self):
        self.screen.blit(self.image, self.rect)

    def reset_player(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update_player(self):
        if self.player_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        elif self.player_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        self.rect.x = self.x
