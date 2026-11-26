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
        self.y = float (self.rect.y)

        self.movement_right = False
        self.movement_left = False
        self.movement_down = False
        self.movement_up = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.movement_right == True and self.x < 1140:
            self.x += self.settings.ship_speed

        if self.movement_left == True and self.x > 0:
            self.x -= self.settings.ship_speed

        if self.movement_up == True and self.y > 500:
            self.y -= self.settings.ship_speed

        if self.movement_down == True and self.y <= 740:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

