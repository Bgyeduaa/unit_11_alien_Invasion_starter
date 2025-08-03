"""
gamestats.py

This module defines the GameStats class used to track and manage player statistics
during gameplay, including score, high score, level, and remaining lives.

Author: Belinda Gyeduaa
"""
from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

""" Tracks and manages statistics for the Alien Invasion game."""
class GameStats():

    """
    __init__ Initialize statistics and load any saved high scores.
    """
    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    """
    Loads the high score from a JSON file if it exists.
    Initializes the file if it does not exist or is empty.
    """
    def init_saved_scores(self) -> None:
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            if not contents:
                print("file empty")
            scores = json.loads(contents)
            self.hi_score = scores.get("hi_score", 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file

    """
    Saves the high score to a JSON file for future game sessions.
    """
    def  save_scores(self) ->None:
        scores = {
            "hi_score": self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    """
    Resets dynamic stats at the start of a game or level.
    Includes score, level, and remaining ships.
    """
    def reset_stats(self) -> None:
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1


    """
    Updates score-related stats after a successful alien collision.
    """
    def update(self, collisions) -> None:
        # update score
        self._update_score(collisions)
        # update max_score
        self._update_max_score()
        # update hi_score
        self._update_hi_score()

    
    """
    Updates the maximum score for the current session if the new score is higher.
    """
    def _update_max_score(self):
        if self.score > self.max_score:
             self.max_score = self.score
        # print(f"Max: {self.max_score}")

    """ Updates the saved high score if the current score exceeds it."""
    def _update_hi_score(self):
        if self.score > self.hi_score:
             self.hi_score = self.score
        # print(f"Hi: {self.hi_score}")

    """ Increases the current score based on the number of alien collisions.""" 
    def _update_score(self, collisions) -> None:
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f"Basic: {self.score}")

    """
    Increments the level when all aliens are destroyed.
    """
    def update_level(self) -> None:
        self.level += 1
        print(self.level)


    

