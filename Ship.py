import pygame
import sys


class Ship(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load("images//Ship1.png")
        self.image.convert_alpha()
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self, ticks):
        # print(self.frame)
        if self.moving_right:
             self.image_rect.x += self.settings.ship_speed * ticks
             if self.image_rect.x > self.settings.screen_w + 128:
                self.image_rect.x = -128
        if self.moving_left:
            self.image_rect.x -= self.settings.ship_speed * ticks
            if self.image_rect.x < -128:
                self.image_rect.x = self.settings.screen_w + 128

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
