class Settings():
    """Klasa odpowiedzialna do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""

        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia statku
        self.ship_speed_factor = 1.5

        # Ustawienia pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 18
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3