import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Load and resize enemy image
        image = pygame.image.load('Assets/astroid.bmp')
        image_size = (50, 50)
        self.image = pygame.transform.scale(image, image_size)

        # Gets positioning information and sets starting location
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Revisit! Store exact horizontal locations, but I don't quite understand how.
        self.x = float(self.rect.x)
