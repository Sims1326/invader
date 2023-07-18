
import pygame
from settings import Settings
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load and resize enemy image
        image = pygame.image.load('Assets/astroid.bmp')

        if image.get_alpha() is None:
            image = image.convert_alpha()

        image_size = (50, 50)
        image = pygame.transform.scale(image, image_size)

        self.image = image
        # Gets positioning information and sets starting location
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Revisit! Store exact horizontal locations, but I don't quite understand how.
        self.x = float(self.rect.x)

    def check_screen_collision(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # Enemy movement
        self.x += (self.settings.enemy_latteral_speed *
                   self.settings.enemy_direction)
        self.rect.x = self.x
