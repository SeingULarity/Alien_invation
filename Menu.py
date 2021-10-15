import pygame
class Menu():
    def __init__(self, ai_game):
        self.game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("Images/Menu.gif").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.settings.screen_w, self.settings.screen_h))
        self.image_rect = self.image.get_rect()


    def main_menu(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game.main()
            self.screen.blit(self.image, self.image_rect)
            pygame.display.update()

