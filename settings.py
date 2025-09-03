class Settings:
    """
    A class to store all settings for Alien Invasion
    """

    def __init__(self):
        """
        Initialize the game's settings.
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        
        # Ship settings
        self.ship_speed = 5

        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (168,50,50)
        self.bullets_allowed = 3