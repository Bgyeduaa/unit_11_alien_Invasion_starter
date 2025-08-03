"""
arsenal.py

Manages the ship's arsenal of bullets in Alien Invasion.
Handles bullet creation, updates, rendering, and removal.

Author: Belinda Gyeduaa
"""
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

"""A class to manage the ship's bullets in the Alien Invasion game.""" 
class Arsenal:

    """Initialize the Arsenal with a reference to the game and create a sprite group for bullets."""
    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    """Update the positions of all bullets and remove those that have moved off-screen"""
    def update_arsenal(self) -> None:
        self.arsenal.update()
        self._remove_bullets_offscreen()

    """Remove bullets that have moved off the top of the screen to free memory."""
    def _remove_bullets_offscreen (self) -> None:
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    """Draw all bullets currently in the arsenal onto the screen."""
    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()

    """ Create and add a new bullet to the arsenal if the maximum allowed bullets
    on screen has not been reached."""
    def fire_bullet(self) -> bool:
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
