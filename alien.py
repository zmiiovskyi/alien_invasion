import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту"""
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizantal position
        self.x = float(self.rect.x)

    def check_edge(self):
        """Повертає істину, якщо прибулець знаходиться на краю екрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Змістити прибульця праворуч чи ліворуч"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_drop_speed)
        self.rect.x = self.x
