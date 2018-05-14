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