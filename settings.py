"""
settings.py
This module defines the Settings class, which contains all configuration 
variables for the Alien Invasion game, including screen size, asset paths, 
game speeds, scoring, UI appearance, and dynamic difficulty settings.

Author: Belinda Gyeduaa
"""

from pathlib import Path
""" A class to store all static and dynamic settings for the Alien Invasion game."""
class Settings: 

    """Initialize the game's static settings, such as screen dimensions, image/sound/font paths,
    UI appearance, and initial game values."""
    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 600
        self.FPS = 60

        """Background image bg_02_h.png from OpenGameArt.ord https://opengameart.org/art-search?keys=starscape"""

        self.bg_file = Path.cwd() / "Assets"/ "images" / "bg_02_h.png" 
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / "Assets"/ "file"/ "scores.json"

        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2_no_bg_removebg.png"
        self.ship_w = 40 
        self.ship_h = 60
        
        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast-removebg.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"

        """sound zapsplat.mp3 from https://www.zapsplat.com/"""

        self.impact_sound = Path.cwd() / "Assets" / "sound" / "zapsplat.mp3"
       
        """facebloom from https://opengameart.org/art-search?keys=alien&page=3"""

        self.alien_file = Path.cwd() / "Assets" / "images" / "facebloom.png"
        self.alien_w = 35
        self.alien_h = 35
       
        self.fleet_direction = 1
       
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 38
        self.HUD_font_size = 20

        """ Font: 'Silkscreen-Bold.ttf' from Google Fonts"""

        self.font_file = Path.cwd() / "Assets"/ "Fonts" / "Silkscreen" / "Silkscreen-Bold.ttf"

    """
    Initialize settings that change throughout the game, such as ship speed,
    bullet speed, and fleet speed. Called when starting or restarting the game.
    """
    def initialize_dynamic_settings(self) ->None:
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50

    """
    Increase the game's difficulty by scaling up movement speeds.
    Called when the player progresses to the next level.
    """     
    def increase_difficulty(self) -> None:
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

