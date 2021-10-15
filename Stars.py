import pygame
from Settings import Settings
class Stars():
    def __init__(self, ai_game):
        pygame.sprite.Sprite.__init__(self)
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load("images/sacura.jpg")
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.settings.screen_w, self.settings.screen_h))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

    def update(self, moving_right, moving_left, ticks):
        if moving_right:
            self.image_rect.x -= self.settings.bg_speed * ticks
        if moving_left:
            self.image_rect.x += self.settings.bg_speed * ticks
        if moving_left == False and moving_right == False:
            if self.image_rect.x < 0:
                self.image_rect.x += self.settings.bg_speed * ticks
            if self.image_rect.x > 0:
                self.image_rect.x -= self.settings.bg_speed * ticks

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
