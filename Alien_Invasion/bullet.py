import pygame

class Bullet:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Alien_Invasion/images/bullet.bmp')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()

        self.rect.midbottom = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

        #Settings 
        self.settings = ai_game.settings

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y -= 5
        self.rect.y = self.y

    def is_off_screen(self):
        return self.rect.bottom <= 0