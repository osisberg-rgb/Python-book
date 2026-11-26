import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Alien_invasion/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.movement_right = False
        self.movement_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movement_right == True:
            self.rect.x += 1

        if self.movement_left == True:
            self.rect.x -= 1

