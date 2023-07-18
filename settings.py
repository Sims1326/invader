import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.game_active = True

        # Player settings
        self.player_speed = 0.75
        self.lives = 3

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_w = 3.0
        self.bullet_h = 15.0
        self.bullet_color = (60, 60, 60)

        # Enemy settings
        self.enemy_latteral_speed = .3
        self.enemy_vertical_speed = 10
        self.enemy_direction = 1
