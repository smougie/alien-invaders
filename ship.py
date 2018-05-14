import pygame

class Ship():
    """Klasa przedstawiająca statek gracza"""

    def __init__(self, screen, ai_settings):
        """Inicjalizacja statku kosmicznego gracza wraz z początkowym położeniem."""

        # Zmienna określająca ekran na którym ma się wyświetlić obiekt klasy Ship()
        self.screen = screen
        self.ai_settings = ai_settings

        # Wczytanie obrazku statku oraz pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.png').convert_alpha()  # Wczytanie custom image dla statku
        self.rect = self.image.get_rect()  # Atrybut powierzchni rect(prostokąt)
        self.screen_rect = screen.get_rect()

        # Każdy nowy statek pojawia się na dole ekranu
        self.rect.centerx = self.screen_rect.centerx  # Środek osi X
        self.rect.bottom = self.screen_rect.centery = 790  # Środek osi Y 790 od górnej krawędzi

        # Punkt środkowy osi X statku przechowywany w postaci liczby zmiennoprzecinkowej.
        self.center = float(self.rect.centerx)

        # Opcja wskazująca na poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie opcji wskazującej na jego ruch, prędkość ustalana w settings."""
        if self.moving_right and (self.rect.right < self.screen_rect.right):  # ograniczenie możliwości ruchu poza ekran
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and (self.rect.left > self.screen_rect.left):  # ograniczenie możliwości ruchu poza ekran
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center  # uaktualnienie obiektu rect na podstawie wartości self.center

    def blitme(self):
        """Wyświetlenie statku kosmicznego w zdefiniowanym położeniu."""
        self.screen.blit(self.image, self.rect)