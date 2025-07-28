from pathlib import Path
class Settings:

    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets"/ "images" / "Starbasesnow.png"

        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2_no_bg_removebg.png"
        self.ship_w = 40 
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast-removebg.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "zapsplat.mp3"
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / "Assets" / "images" / "facebloom.png"
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2
        self.fleet_direction = 1
        self.fleet_drop_speed = 40

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 38
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / "Asset"/ "Fonts" / "Silkscreen" / "Silkscreen-Bold.ttf"
