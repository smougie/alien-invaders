import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedynczego obcego"""

    def __init__(self, ai_settings, screen):
        """Inicjalizacja obcego i zdefiniowanie jego położenia."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytanie obrazu dla statku oraz zdefiniowanie atrybutu rect.
        self.image = pygame.image.load('images/alien.png').convert_alpha()
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w pobliżu lewego górnego rogu
        self.rect.x = self.rect.width  # ustawienie odległości od lewej strony ekranu (odległość = szerokość obcego)
        self.rect.y = self.rect.height  # Ustawienie odległości od góry ekranu (odległość = wysokość obcego)

        # Przechowanie dokładnego położenia obcego.
        self.x = float(self.rect.x)

    def blitme(self):
        """Wyświetlenie obcego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Zwraca wartość True, jeżeli obcy znajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()  # Zapisujemy w zmiennej wartość kwadratu okna
        if self.rect.right >= screen_rect.right:  # Sprawdzamy czy prawa krawędz prostokąta obcego jest >=
                                                  # prawej krawędzi ekranu
            return True
        elif self.rect.left <= 0:  # Sprawdzamy czy lewa krawędz obcego jest <= wartości 0 oznaczającej lewą krawędź
                                   # ekranu
            return True

    def update(self):
        """Przesunięcie obcego w lewo lub w prawo - jeżeli wartością fleed_direction jest 1(prawo) to speed_factor
           zostanie dodany do X. Jeżeli wartością fleet_direction jest -1(lewo) to speed_factor zostanie odjęty od X."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x