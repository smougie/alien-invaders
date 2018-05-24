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


def update_alien(aliens):
    """Uaktualnienie położenia każdego obcego."""
    aliens.update()


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """Uaktualnienie pocisków.
       Wywołanie metody update dla grupy bullets wywołuje update dla każdego sprite'a w grupie.
       collisions - powoduje przeprowadzenie iteracji przez wszystkie pociski oraz przez wszystkich obcych, jeżeli
       funkcja wykryje kolizję, któregokolwiek z elementów bullets lub aliens to dzięki kolejnym argumentom ustawionym
       na True, usunie element z bullet i alien, jeżeli ustawimy argument na False, element nie zostanie usunięty"""
    bullets.update()
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:  # Sprawdzany ilość obcych na ekranie
        bullets.empty()  # Usuwamy wszystkie pociski
        create_fleet(ai_settings, screen, ship, aliens)  # Tworzymy nową flotę

    # Usunięcie pocisków znajdujących się poza ekranem - y <= 0
    for bullet in bullets.copy():  # Wewnątrz pętli for nie należy usuwać elementów listy dlatego używamy copy()
        if bullet.rect.bottom <= 0:  # Jeżeli dolna krawędź bullet <= 0
            bullets.remove(bullet)


def fire_bullet(bullets, ai_settings, screen, ship):
    """Funkcja odpowiedzialna za wystrzelenie pocisku jeżeli nie przekroczono określonego limitu."""
    if len(bullets) < ai_settings.bullets_allowed:  # Ograniczenie ilości posiadanych pocisków do 3
        new_bullet = Bullet(ai_settings, screen, ship)  # W zmiennej tworzy nowy obiekt klasy Bullet()
        bullets.add(new_bullet)  # Dodaje stworzony obiekt do grupy pocisków bullets


def get_number_aliens_x(ai_settings, alien_width):
    """Funkcja odpowiedzialna za obliczenia pola przeznaczonego do wyświetlania obcych, szerokość ekranu odjąć margines
    z lewej i margines z prawej które wynoszą szerokość obcego z każdej strony."""
    available_space_x = ai_settings.screen_width - (2 * alien_width)  # 1080

    # Ilość obcych znajdujących się w obszarze available_space_x wynosi pole wyznaczone do wyświetlenia podzielone przez
    # szerokość statków razy dwa, każdy statek musi mieć odstęp jednego statku
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 9

    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Funkcja odpowiedzialna za ustalenie ile rzędów obych zmieści się na ekranie."""
    # Ustalenie dostępnego miejsca - wysokość ekranu - wysokość 3 obcych -  wysokość statku gracza
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height

    # Ilość rzędów to ilość dostępnego miejsca podzielona przez dwukrotną wysokość statku, wliczono odstęp o wartości
    # wysokości jednego obcego
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w rzędzie.
    # Odległość między poszczególnymi obcymi jest równa szerokości obcego
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # Zmieniamy wartość współrzędnej Y obcego tak aby znajdował się w odległości jednego obcego od górnej krawędzi
    # ekranu, a każdy rząd rozpoczynał się dwie wysokości obcego poniżej poprzedniego rzędu:
    #  2 * wysokość obcego * row_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Funkcja odpowiedzialna z autworzenie floty obcych."""
    alien = Alien(ai_settings, screen)  # Utworzenie obcego
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  # Sprawdzenie ilu obcych zmieści się w rzędzie
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)  # Ustalenie ile rzędów dla obcych

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Odpowiednia reakcja na to kiedy obcy dotrze do krawędzi ekanu."""
    for alien in aliens.sprites():
        if alien.check_edges():  # Jeżeli któryś obcy znajdzię się przy prawej krawędzi ekranu trzeba zmienić direction
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Przesunięcie całej floty w dół i zmiana kierunku, w którym się prousza"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """Sprawdzenie czy flota znajduje się przy krwędzi ekranu, a następnie uaktualnienie położenia wszystkich obcych"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()