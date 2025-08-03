"""
bullet.py

Defines the Bullet class for the Alien Invasion game.
Handles bullet image loading, movement updates, and rendering.

Author: Belinda Gyeduaa
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

"""A class to manage individual bullets fired by the ship."""
class Bullet(Sprite):

    """Initialize a bullet object at the ship's current position."""
    def __init__(self, game: "AlienInvasion") ->None:
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    """Move the bullet upward on the screen based on the configured bullet speed."""
    def update(self) -> None:
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    """Draw the bullet to the screen at its current location."""
    def draw_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)
        
