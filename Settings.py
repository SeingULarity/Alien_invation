import pygame
class Settings():
    def __init__(self):
        # Screen
        self.screen_w = 800
        self.screen_h = 600
        self.bg_color = (105, 105, 105)
        # Main world Settings
        self.frame_rate = 60
        # object properties
        self.ship_speed = 0.5  # Ship speed
        self.health = 100
        self.bg_speed = 0.3  # Background bad animation
        self.hardness = 0.5
        # Bullet properties
        self.bullet_speed = 0.2
        self.bullet_w = 3
        self.bullet_h = 15
        self.bullet_c = (50, 50, 50)
        self.coldown = 100
        # Buff properties
        self.buff_speed = 0.3
        self.coldown_buf = 5000
        self.buff_pos_x = [100, 200, 300, 400, 500, 600, 700]
        #
        self.score = 0
        # alien properties
        self.alien_speed = 0.1
        self.fleet_drop_speed = 0.1
        self.fleet_direction = +1
        self.coldown_spawn = 3000