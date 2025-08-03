"""button.py

Defines the Button class for Alien Invasion. This class handles creating,
rendering, and checking user interaction with the game's on-screen button.

Author: Belinda Gyeduaa
"""
import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

""" A class to represent an interactive button in the Alien Invasion game."""
class Button:

    """ Initialize the button's attributes, including its size, position,
    font, color, and the label to be displayed."""
    def __init__(self, game: "AlienInvasion", msg) -> None:
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    """ Render the message text into an image and center it on the button rectangle."""
    def _prep_msg(self, msg) -> None:
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    """Draw the button onto the screen, including its background and message text."""
    def draw(self) -> None: 
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    """Check whether the button has been clicked based on mouse position."""
    def check_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    