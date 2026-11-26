import pygame
import sys


class CheckEvent:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.ship = ai_game.ship


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


            self.key_movement(event)
            

    def key_movement(self, event):
        #Pressing keys down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.movement_right = True

            if event.key == pygame.K_LEFT:
                self.ship.movement_left = True

            if event.key == pygame.K_UP:
                self.ship.movement_up = True

            if event.key == pygame.K_DOWN:
                self.ship.movement_down = True

            if event.key == pygame.K_SPACE:
                self.ai_game.fireBullet()

        #Relizing the keys
        elif event.type == pygame.KEYUP:

            #Right arrow
            if event.key == pygame.K_RIGHT:
                    self.ship.movement_right = False

            #Left arrow
            if event.key == pygame.K_LEFT:
                self.ship.movement_left = False

            #Up arrown 
            if event.key == pygame.K_UP:
                self.ship.movement_up = False

            #Down arrow
            if event.key == pygame.K_DOWN:
                self.ship.movement_down = False

