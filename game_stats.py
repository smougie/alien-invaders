class GameStats():
    """Monitorowanie danych statystycznych."""

    def __init__(self, ai_settings):
        """Inicjalizacja danych satystycznych."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False  # Uruchamiamy grę w stanie nieakwtywnym
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Inicjalizacja danych statystyczncyh, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
