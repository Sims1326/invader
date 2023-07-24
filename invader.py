import sys
from time import sleep
import pygame
import math
from bullet import Bullet
from start_button import Button
from scoreboard import Scoreboard
from settings import Settings
from stats import Stats
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
        self.stats = Stats(self)
        self.score = Scoreboard(self)
        self.start_button = Button(self, "Play")
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_start(pygame.mouse.get_pos())

    def check_start(self, mouse_position):
        if self.start_button.rect.collidepoint(mouse_position):
            self.settings.game_active = True
            self.stats.reset()
            self.score.prep_level()
            self.score.prep_lives()

    def fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def updated_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.draw_player()
        self.enemies.draw(self.screen)
        self.score.show_score()
        if not self.settings.game_active:
            self.start_button.draw_button()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True)
        if collisions:
            for ennemy in self.enemies.sprites():
                self.stats.points += self.settings.enemy_point_value
                self.score.prep_score()
                self.score.check_hs()
        if not self.enemies:
            self.bullets.empty()
            self.make_enemy()
            self.settings.level_up()
            self.score.prep_level()

    def make_enemy(self):
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        available_space = self.settings.screen_width - (2 * enemy_width)
        enemies_on_screen = math.floor(available_space / (enemy_width * 2))
        space_y = (self.settings.screen_height -
                   (6 * enemy_height) - self.player.rect.height)
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

    def enemy_movement(self):
        for enemy in self.enemies.sprites():
            if enemy.check_screen_collision():
                self.pivot_enemies()
                break

    def pivot_enemies(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.enemy_vertical_speed

        self.settings.enemy_direction *= -1

    def update_enemies(self):
        self.enemy_movement()
        self.enemies.update()

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.ship_hit()
        self.check_ship_location()

    def check_ship_location(self):
        screen_rect = self.screen.get_rect()
        for enemy in self.enemies.sprites():
            if enemy.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    def ship_hit(self):
        if self.settings.lives > 0:
            self.settings.lives -= 1
            self.score.prep_lives()
            self.enemies.empty()
            self.bullets.empty()

            self.make_enemy()

        else:
            self.bullets.empty()
            self.enemies.empty()
            self.settings.game_active = False

        sleep(1)

    def run_game(self):
        while True:
            self.check_events()
            if self.settings.game_active:
                self.player.update_player()
                self.update_bullets()
                self.update_enemies()
            self.updated_screen()


if __name__ == "__main__":
    invaders = Invaders()
    invaders.run_game()
