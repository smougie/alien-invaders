import sys

import pygame

from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Funkcja nasłuchuje zdarzeń podczas pętli."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Jeżeli gracz naciśnie X w prawym górnym rogu, następuje zamknięcie okna
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Jeżeli zostanie wciśnięty klawisz
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # Jeżeli klawisz zostanie zwolniony
            check_keyup_events(event, ai_settings, screen, ship, bullets)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Funkcja odpowiedzialna za obsługę eventów związanych z wciśnięciem klawisza."""
    if event.key == pygame.K_RIGHT:  # Sprawdza jaki klawisz został wciśniety
        ship.moving_right = True  # Zmienia wartość moving_right w obiekcie klasy Ship() na True
    elif event.key == pygame.K_LEFT:  # Sprawdza jaki klawisz został wciśniety
        ship.moving_left = True  # Zmienia wartość moving_left w obiekcie klasy Ship() na True
    elif event.key == pygame.K_SPACE:  # Sprawdza jaki klawisz został wciśnięty
        fire_bullet(bullets, ai_settings, screen, ship)  # Wywołanie funkcji odpowiedzialnej za wystrzelenie pocisku
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    """Funkcja odpowiedzialna za obsługę eventów związanych ze zwolnieniem klawisza."""
    if event.key == pygame.K_RIGHT:  # Sprawdza który klawisz został zwolniony
        ship.moving_right = False  # Zmienia wartość moving_right w obiekcie klasy Ship() na False
    elif event.key == pygame.K_LEFT:  # Sprawdza który klawisz został zwolniony
        ship.moving_left = False  # Zmienia wartość moving_left w obiekcie klasy Ship() na False


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    screen.fill(ai_settings.bg_color)  # Wypełnienie tła przy użyciu klasy obiektu klasy Settings()

    # Ponowne wyświetlenie wszystkich pocisków pod warstwą ship i aliens
    for bullet in bullets:
        # bullet.draw_bullet()  # Tworzy obiekt przy użyciu metody draw_bullet, klasy Bullet()
        screen.blit(bullet.image, bullet.rect)  # Tworzy obiekt wypełniony przez wskazany image
    ship.blitme()  # Wyświetlenie statku na ekranie, "nad" kolorem tła oraz nad pociskami
    aliens.draw(screen)  # Wyświetlenie obcego na ekranie
    pygame.display.flip()  # Wyświetlenie ostatnio zmodyfikowanego ekranu - odświeżanie


def update_bullets(bullets):
    """Uaktualnienie pocisków"""
    bullets.update()  # Wywołanie metody update dla grupy bullets wywołuje update dla każdego sprite'a w grupie

    # Usunięcie pocisków znajdujących się poza ekranem - y <= 0
    for bullet in bullets.copy():  # Wewnątrz pętli for nie należy usuwać elementów listy dlatego używamy copy()
        if bullet.rect.bottom <= 0:  # Jeżeli dolna krawędź bullet <= 0
            bullets.remove(bullet)

def fire_bullet(bullets, ai_settings, screen, ship):
    """Funkcja odpowiedzialna za wystrzelenie pocisku jeżeli nie przekroczono określonego limitu"""
    if len(bullets) < ai_settings.bullets_allowed:  # Ograniczenie ilości posiadanych pocisków do 3
        new_bullet = Bullet(ai_settings, screen, ship)  # W zmiennej tworzy nowy obiekt klasy Bullet()
        bullets.add(new_bullet)  # Dodaje stworzony obiekt do grupy pocisków bullets

def create_fleet(ai_settings, screen, ship, bullets, aliens):
    """Utworzenie floty obcych"""

    # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w rzędzie.
    # Odległość między poszczególnymi obcymi jest równa szerokości obcego
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    # Pole przeznaczone do wyświetlania obcych, szerokość ekranu odjąć margines z lewej i margines z prawej które
    # wynoszą szerokość obcego z każdej strony
    available_space_x = ai_settings.screen_width - (2 * alien_width)  # 1080

    # Ilość obcych znajdujących się w obszarze available_space_x wynosi pole wyznaczone do wyświetlenia podzielone przez
    # szerokość statków razy dwa, kazdy statek musi mieć odstęp jednego statku
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 9

    # Utworzenie pierwszego rzędu obcych
    for alien_number in range(number_aliens_x):
        # Utworzenie obcego i umieszczenie go w rzędzie
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
