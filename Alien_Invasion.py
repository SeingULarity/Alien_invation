import sys
from Settings import Settings
from Ship import Ship
from Stars import Stars
from Bullet import Bullet
from Buf import Buf
from alien import Alien
from Menu import Menu
from dead_window import DeadWindow
import pygame


class AlienInvasion:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.game_is_running = True
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))


        self.ship = Ship(self)
        self.stars = Stars(self)
        self.menu = Menu(self)
        self.buffs = pygame.sprite.Group()

        self.spawn_buff = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_buff, self.settings.coldown_buf)

        self.spawn_fleet = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_fleet, self.settings.coldown_spawn)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()


        self.clock = pygame.time.Clock()

        self.begin = pygame.time.get_ticks() #Time zero
        self.time_for_buf = pygame.time.get_ticks()
        self.current_time = 0
        self.moment_time = 0
        self.fired = False
        self.is_paused = False
        self.game_is_running = True
# Main loop
    def run_game(self):
        while self.game_is_running:
            self.dt = pygame.time.get_ticks() - self.begin
            #print(pygame.time.get_ticks() / 1000)
            # dt *= self.settings.frame_rate
            self.begin = pygame.time.get_ticks()

            self._check_events()
            self.ship.update(self.dt)
            self.stars.update(self.ship.moving_right, self.ship.moving_left, self.dt)
            self._update_bullets()
            self.fire_bullet()
            self._update_buffs()
            self._check_collition_buf()
            self._update_aliens()
            if self.settings.health == 0 or not self.game_is_running:
                self.show_dead_window()
                self.game_is_running = False


            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    self.fired = True
                if event.key == pygame.K_ESCAPE:
                    self.game_is_running = False

                if event.key == pygame.K_f:
                    self.__name__ = '__main__'
                    #self.game_is_running = True
                    print('f')
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    self.fired = False
            if event.type == self.spawn_buff:
                if len(self.aliens) < self.number_aliens_x:
                    self._spawn_buf()
            if event.type == self.spawn_fleet:
                if len(self.aliens) == 0:
                    self.settings.alien_speed += 0.1
                    self.settings.fleet_drop_speed += 0.1
                    self._create_fleet()

    def fire_bullet(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.time_for_buf > self.settings.coldown and self.fired == True:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.time_for_buf = pygame.time.get_ticks()

    def _update_bullets(self):
        self.bullets.update(self.dt)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        if pygame.sprite.groupcollide(self.bullets, self.aliens, True, True):
            self.settings.score += 1

    def _spawn_buf(self):
        new_buf = Buf(self)
        self.buffs.add(new_buf)

    def _update_buffs(self):
        self.buffs.update(self.dt)
        for buff in self.buffs.copy():
            if buff.image_rect.top >= self.settings.screen_h:
                self.buffs.remove(buff)

    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)

        self.stars.blitme()
        if self.game_is_running:
            for buff in self.buffs.sprites():
                buff.blitme()
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw()
            self.aliens.draw(self.screen)
        self._show_score()

        pygame.display.flip()
        self.clock.tick(self.settings.frame_rate)
        pygame.display.set_caption(f"Alien Game     [FRAME TIME: {int(self.clock.get_fps())}]")

    def _create_buf(self):
        self.create_buf = pygame.USEREVENT
        pygame.time.set_timer(self.create_buf, self.settings.coldown_buf)

    def _check_collition_buf(self):
        for buf in self.buffs:
            if self.ship.image_rect.colliderect(buf.image_rect):
                self.buffs.remove(buf)
        for alien in self.aliens:
            if self.ship.image_rect.colliderect(alien.rect):
                if self.settings.health > 0:
                    self.settings.health -= self.settings.hardness

                # self.settings.score += 1


    def _show_score(self):
        heath_surface = pygame.font.SysFont('bahnschrift', 28)
        heathboard = heath_surface.render(f"Hp: {int(self.settings.health)}", True, (255, 0, 0))
        score_surface = pygame.font.SysFont('arial', 25)
        scoreboard = score_surface.render(f'Score: {self.settings.score}', True, (255, 255, 255))
        self.screen.blit(heathboard, (0, 28))
        self.screen.blit(scoreboard, (0, 0))
        #print(pygame.font.get_fonts())

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_w - (2 * alien.rect.width)
        self.number_aliens_x = available_space_x // (2 * alien.rect.width)
        available_space_y = self.settings.screen_h - (3 * alien_height) - self.ship.image_rect.height
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(self.number_aliens_x):
                self._create_alien(row_number, alien_number)

    def _create_alien(self, row_number, alien_number):
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_out_fov()
        self._check_edjes()
        self.aliens.update(self.dt)

    def _check_out_fov(self):
        for alien in self.aliens.sprites():
            if alien.check_out_of_fov():
                self.aliens.remove(alien)

    def _check_edjes(self):
        for alien in self.aliens.sprites():
            if alien.check_edjes():
                self._chenge_fleet_direction()
                break


    def _chenge_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed * self.dt
            #print(alien.rect.y)
        self.settings.fleet_direction *= -1

        #print(self.settings.fleet_direction)

    def show_dead_window(self):
        dead_window = DeadWindow(self.settings.score, pygame.time.get_ticks() / 1000)
        dead_window.run()






if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
