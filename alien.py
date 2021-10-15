import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("Images/Alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edjes(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
    def check_out_of_fov(self):
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def update(self, ticks):
        self.x += self.settings.fleet_direction * (self.settings.alien_speed * ticks)
        self.rect.x = self.x

    def update_y_pos(self, ticks):
        self.y += self.settings.fleet_drop_speed * ticks
        self.rect.y = self.y
        print(self.rect.y)
