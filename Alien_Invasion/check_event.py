import pygame
import sys


class CheckEvent:

    def __init__(self, ai_game):
        self.ship = ai_game.ship

        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.movement_right = True

                if event.key == pygame.K_LEFT:
                    self.ship.movement_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.movement_right = False

                if event.key == pygame.K_LEFT:
                    self.ship.movement_left = False