import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manager game assets and behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            print(self.ship.moving_right)
            self.ship.update()
            self._update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()

    def _check_events(self):
        # Respond to key presses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                self.ship.rect.x += 1

    def _update_screen(self):
        # Update images on the screen, and flip to new screen.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
