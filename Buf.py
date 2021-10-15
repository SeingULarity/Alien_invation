import pygame, random
from pygame.sprite import Sprite
class Buf(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/But.png")
        self.image.convert_alpha()
        self.random_pos = random.choice(self.settings.buff_pos_x)
        self.image_rect = self.image.get_rect(midtop = (self.random_pos, -34))
        self.y = float(self.image_rect.y)

    def update(self, ticks):
        self.y += self.settings.buff_speed * ticks
        self.image_rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
