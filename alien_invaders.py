import pygame
from pygame.sprite import Group

from button import Button
from settings import Settings
from game_stats import GameStats
from ship import Ship
from game_functions import check_events, update_screen, update_bullets, create_fleet, update_aliens


def run_game():

    """Inicjalizacja gry."""
    pygame.init()
    ai_settings = Settings()  # Import ustawień z klasy Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Rozdzielczość ekranu
    pygame.display.set_caption('Alien Invaders')  # Nazwa okna

    play_button = Button(ai_settings, screen, 'Gra')  # Utworzenie przycisku Gra na środku ekranu
    stats = GameStats(ai_settings)  # Utworzenie obiekt klasy GameStats do przechowywania danych statystycznych gry
    ship = Ship(screen, ai_settings)  # Tworzymy obiekt klasy Ship()
    bullets = Group()  # Grupa przeznaczona do przechowywania pocisków
    aliens = Group()  # Grupa przeznaczona do przechowywania obcych
    create_fleet(ai_settings, screen, ship, aliens)  # Utworzenie floty obcych

    # Rozpoczęcie głównej pętli gry.
    while True:

        # Moduły odpowiedzialne za odświeżanie ekranu po każdej iteracji pętli.
        check_events(ai_settings, screen, ship, bullets)  # Nasłuchuje zdarzeń (eventów)
        if stats.game_active:
            ship.update()  # Uaktualnia położenie statku
            update_bullets(ai_settings, screen, ship, bullets, aliens)  # Uaktualnia pociski oraz usuwa pociski znajdujące
            # się poza ekranem, odpowiada za utworzenie nowej nowej floty po zniszczeniu wszystkich obcych

            update_aliens(ai_settings, stats, screen, aliens, ship, bullets)  # Uaktualnie flotę obcych, ustala położenie
            # oraz kierunek poruszania

        update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button)  # Uaktualnienie obrazów i przejście do
        # nowego ekranu


run_game()
