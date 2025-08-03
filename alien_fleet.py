"""
alien_fleet.py

This module contains the AlienFleet class which manages the creation, positioning,
movement, and behavior of the alien enemies in the Alien Invasion game.

Author: Belinda Gyeduaa
Assets Used:
    - Alien image: facebloom.png (https://opengameart.org/art-search?keys=alien&page=3)
"""

import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

""" Manages the alien fleet for the Alien Invasion game."""
class AlienFleet:
    def __init__(self, game: "AlienInvasion") -> None:
        """ Initialize the fleet with reference to the main game instance.
"""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        
        self.create_fleet()

    """
    Creates the initial fleet of aliens using a rectangular grid formation.
    """
    def create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, screen_h, fleet_w, fleet_h)

        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    """
    Creates a full rectangular grid of aliens.
"""
    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset) -> None:
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 ==0: # modified on 8/2
                    continue

                self._create_alien(current_x, current_y)

    """Center the rectangle horizontally; place vertically centered in the top half"""
    def calculate_offsets(self, alien_w, alien_h, screen_w, screen_h, fleet_w, fleet_h) -> tuple[int, int]:
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h

        x_offset = int((screen_w - fleet_horizontal_space) // 2)
        y_offset = int(((screen_h // 2) - fleet_vertical_space) // 2)
        return x_offset, y_offset

    """Fit as many aliens as possible into a centered grid in the top half"""
    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h) -> tuple[int, int]:
        fleet_w = (screen_w // alien_w) 
        fleet_h = ((screen_h // 2) // alien_h)
        
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        fleet_w = max(fleet_w, 1)
        fleet_h = max(fleet_h, 1)
        return int(fleet_w), int(fleet_h)

    """
    Creates a single alien at the specified position and adds it to the fleet.
    """
    def _create_alien(self, current_x: int, current_y: int) -> None:
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    """
    Checks if any alien has reached the screen edge and triggers a downward drop if needed.
    """
    def _check_fleet_edges(self) -> None:
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

        """
        Moves all aliens in the fleet downward by the defined drop speed.
        """
    def _drop_alien_fleet(self) -> None:
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    """
    Updates the position of all aliens and handles edge behavior.
    """
    def update_fleet(self) -> None:
        self._check_fleet_edges()
        self.fleet.update()

    """
    Draws all aliens on the screen.
    """
    def draw(self) -> None:
        for alien in self.fleet:
            alien.draw_alien()

    """
     Checks for collisions between the fleet and another sprite group (e.g., bullets).
    """
    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    """
    Checks if any alien has reached the bottom of the screen.
    """
    def check_fleet_bottom(self) -> bool:
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    """
    Checks if the entire fleet has been destroyed.
    """
    def check_destroyed_status(self) -> bool:
        return not self.fleet
