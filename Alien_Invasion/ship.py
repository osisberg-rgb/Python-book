import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Alien_invasion/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        #Settings 
        self.settings = ai_game.settings

        self.rect.midbottom = self.screen_rect.midbottom

        #Store Float
        self.x = float(self.rect.x)

        self.movement_right = False
        self.movement_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movement_right == True:
            self.x += self.settings.ship_speed

        if self.movement_left == True:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

