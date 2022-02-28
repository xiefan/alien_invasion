import pygame

from pygame.sprite import Sprite
import random

class AsteroidExplosion(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game, posx, posy):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the asteroid image and set its rect attribute
        self.image = pygame.transform.scale(pygame.image.load('images/explosion.png'), (100, 100))
        self.rect = self.image.get_rect()

        #print("Explosion spawn here")
        self.rect.x = posx - 50
        self.rect.y = posy - 50

    def blit(self):
        # Draw the bullet to the screen
        self.screen.blit(self.image, self.rect)