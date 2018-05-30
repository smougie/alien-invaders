import pygame.font

class Scoreboard():
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, ai_settings, screen, stats):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Ustawienia czcionki dla informacji dotyczących punktacji.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie początkowych obrazków z punktacją
        self.prep_score()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        rounded_scrore = int(round(self.stats.score, -1))  # Zaokrąglamy wynik do najbliższej wielokrotności czyli 10
        score_str = '{:,}'.format(rounded_scrore)  # Przekazana wartość liczbowa zostanie oddzielona ',' po osiągnieciu
                                                   # wartości 1000
        self.score_image = self.font.render(score_str, True, self.text_color)  # Renderujemy obraz punktacji

        # Wyświetlenie punktacji w prawym górnym rogu ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Wyświetlenie punktacji na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
