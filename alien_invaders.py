import pygame
from pygame.sprite import Group


from settings import Settings
from ship import Ship
from game_functions import check_events, update_screen, update_bullets, create_fleet


def run_game():

    """Inicjalizacja gry."""
    pygame.init()
    ai_settings = Settings()  # Import ustawień z klasy Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Rozdzielczość ekranu
    pygame.display.set_caption('Alien Invaders')  # Nazwa okna

    ship = Ship(screen, ai_settings)  # Tworzymy obiekt klasy Ship()
    bullets = Group()  # Grupa przeznaczona do przechowywania pocisków
    aliens = Group()  # Grupa przeznaczona do przechowywania obcych

    create_fleet(ai_settings, screen, ship, bullets, aliens)

    # Rozpoczęcie głównej pętli gry.
    while True:

        # Moduły odpowiedzialne za odświeżanie ekranu po każdej iteracji pętli.
        check_events(ai_settings, screen, ship, bullets)  # Nasłuchuje zdarzeń (eventów)
        ship.update()  # Uaktualnia położenie statku
        update_bullets(bullets)  # Uaktualnia pociski oraz usuwa pociski znajdujące się poza ekranem
        update_screen(ai_settings, screen, ship, bullets, aliens)  # Uaktualnienie obrazów i przejście do nowego ekranu


run_game()