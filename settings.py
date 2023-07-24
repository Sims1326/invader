import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.game_active = False
        self.level = 1

        # Player settings
        self.player_speed = 0.75

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_w = 5
        self.bullet_h = 15.0
        self.bullet_color = (60, 60, 60)

        # Enemy settings
        self.enemy_latteral_speed = 10
        self.enemy_vertical_speed = 10
        self.enemy_point_value = self.level * 5 - 2
        self.enemy_direction = 1

        self.enemy_latteral_speed_factor = 1.143
        self.player_speed_factor = 1.121

    def default_settings(self):
        self.lives = 3
        self.enemy_latteral_speed = .3
        self.player_speed = 0.75
        self.level = 1

    def level_up(self):
        self.level += 1
        self.enemy_latteral_speed *= self.enemy_latteral_speed_factor
        self.player_speed *= self.player_speed_factor
