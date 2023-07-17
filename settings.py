import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (248, 144, 231)

        # Player settings
        self.player_speed = 0.75

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_w = 3.0
        self.bullet_h = 15.0
        self.bullet_color = (60, 60, 60)
