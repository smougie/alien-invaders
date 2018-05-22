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

        # Ustawienia obcego
        self.alien_speed_factor = 1  # Szybkość z jaką flota będzie się poruszać w lewo i prawo
        self.fleet_drop_speed = 10  # Szybkość z jaką flota będzie się poruszać w dół ekranu
        self.fleet_direction = 1  # Wartość fleet_diection wynosząca 1 oznacza prawo natomiast -1 oznacze lewo