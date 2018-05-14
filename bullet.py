import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania wystrzeliwanymi przez statek pociskami."""

    def __init__(self, ai_settings, screen, ship):
        """Utworzenie pocisku w aktualnym położeniu statku."""
        super().__init__()
        self.screen = screen

        # Utworzenie prostokąta pocisku w punkcie (0, 0), a następnie zdefiniowanie dla niego odpowiedniego położenia.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # Położenie + rozmiar
        self.image = pygame.image.load('images/green_bullet.png').convert_alpha()  # Wczytanie custom image dla bullet
        self.rect.centerx = ship.rect.centerx  # Wartość położenia pocisku jest taka sama jak statku
        self.rect.top = ship.rect.top  # Górna krawędź pocisku dopasowana do górnej krawędźi statku

        # Położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej w celu dobrej kontroli nad ruchem
        self.y = float(self.rect.y)

        # Kolor oraz prędkość pocisku
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Poruszanie pocisku po ekranie."""
        self.y -= self.speed_factor  # uaktualnienie położenia pocisku, wystrzelony pocisk porusza się w górę ekranu
        self.rect.y = self.y  # uaktualnienie położenia prostokąta pocisku

    def draw_bullet(self):
        """Stworzenie prostokąta pocisku, wypełnienie go kolorem i wyświetlenie na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)