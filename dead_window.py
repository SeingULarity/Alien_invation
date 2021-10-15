import pygame
from Settings import Settings

class DeadWindow:

    def __init__(self, score, play_time):
        pygame.init()
        pygame.font.init()
        font = pygame.font.Font(None, 60)
        self.surface = pygame.display.set_mode((Settings().screen_w, Settings().screen_h))
        pygame.display.set_caption("You are dead!")

        self.play_time = play_time
        self.score = score

        self.text = font.render(f"Time:{self.play_time}, Score:{self.score}", False, (255, 0, 0))

        self.is_dead = False

    def run(self):
        self.is_dead = True
        while self.is_dead:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stop()
            self.draw()
            self.update()

    def stop(self):
        self.is_dead = False

    def draw(self):
        self.surface.fill((255, 255, 255))
        self.surface.blit(self.text, (Settings().screen_w // 2 - 190, Settings().screen_h // 2))

    def update(self):
        pygame.display.update()