import sys

import pygame

from settings import Settings
from ship import Ship
from check_event import CheckEvent
from bullet import Bullet



class AlienInvasion: 
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

        self.bullets = []

        self.check_events = CheckEvent(self)

        pygame.display.set_caption("Alien invasion")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_events._check_events()
            self.ship.update()
            for bullet in self.bullets:
                bullet.update()
            self._update_screen()
            self.clock.tick(60)



    def _update_screen(self):
        #BackGround color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets[:]:
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
            else:
                bullet.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()


    def fireBullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.append(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()