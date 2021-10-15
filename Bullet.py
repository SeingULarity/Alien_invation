import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_c
        self.rect = pygame.Rect(0, 0, self.settings.bullet_w, self.settings.bullet_h)
        self.rect.midtop = ai_game.ship.image_rect.midtop
        self.y = float(self.rect.y)

    def update(self, tick):
        self.y -= self.settings.bullet_speed * tick
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
