import sys
import pygame
import math
from bullet import Bullet
from settings import Settings
from player_character import Player
from enemy import Enemy


class Invaders:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invader")
        self.enemies = pygame.sprite.Group()
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()

        self.make_enemy()

    def check_events(self):
        # Exits Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Player Movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.player_right = True
                    self.player.rect.x += 1
                elif event.key == pygame.K_LEFT:
                    self.player.player_left = True
                    self.player.rect.x -= 1
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()
                elif event.key == pygame.K_q:
                    sys.exit()
            # Stops Player Movement
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.player_right = False
                elif event.key == pygame.K_LEFT:
                    self.player.player_left = False

    def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def updated_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.draw_player()
        self.enemies.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))

    def make_enemy(self):
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        available_space = self.settings.screen_width - (1.8 * enemy_width)
        enemies_on_screen = math.floor(available_space / (enemy_width * 1.8))
        space_y = (self.settings.screen_height -
                   (3 * enemy_height) - self.player.rect.height)
        rows = math.floor(space_y / (enemy_height * 2))
        for row in range(rows):
            for enemy_load in range(enemies_on_screen):
                self.create_enemy(enemy_load, row)

    def create_enemy(self, enemy_load, row):
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.x = enemy_width + 1.8 * enemy_width * enemy_load
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy_height * 3 * row
        self.enemies.add(enemy)

    def run_game(self):
        while True:
            self.check_events()
            self.player.update_player()
            self.update_bullets()
            self.updated_screen()


if __name__ == "__main__":
    invaders = Invaders()
    invaders.run_game()
