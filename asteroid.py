import pygame

from pygame.sprite import Sprite
import random

class Asteroid(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the asteroid image and set its rect attribute
        self.image = pygame.transform.scale(pygame.image.load('images/asteroid.png'), (100, 100))
        self.rect = self.image.get_rect()

        # Start each new asteroid in the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the asteroid's exact horizontal position
        self.x = float(self.rect.x)

        """Draw the asteroid"""
        asteroid_posx = random.randint(0,ai_game.settings.screen_width)
        asteroid_posy = random.randint(250,ai_game.settings.screen_height-500)
        print("I spawned in!!!")
        self.rect.x = asteroid_posx
        self.rect.y = asteroid_posy

    def blit(self):
        # Draw the bullet to the screen
        self.screen.blit(self.image, self.rect)