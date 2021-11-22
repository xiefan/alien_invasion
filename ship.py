import pygame


class Ship:
    # A class to manage the ship

    def __init__(self, ai_game):
        # initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        large_image = pygame.image.load('images/crash_course12-01.png')
        small_image = pygame.transform.scale(large_image, (100, 100))
        self.image = small_image
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect = pygame.display.set_mode((150,150))

        # Movement flag
        self.moving_right = False

    def update(self):
        # Update the ship's position based on the movement flag
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
