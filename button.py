import pygame.font

class Button():
    def __init__(self, ai_setting, screen, msg):
        '''Inicjalizacja artybutuów przycisku.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Zdefiniowanie wymiarów i właściwości przycisku
        self.width, self.hight = 200, 50
        self.button_color = (51, 51, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Utworzenie prostokąta przycisku i wyśrodkowanie go
        self.rect = pygame.Rect(0, 0, self.width, self.hight)
        self.rect.center = self.screen_rect.center

        # Komunikat wyświetlany przez przycisk trzeba przygotować tylko jednokrotnie
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie i wyśrodkowanie tekkstu przycisku"""
        # Wywołanie font render zamienia tekst przechwytywany w msg na obraz, wartość boolowska oznacza wygładzanie krawędzi
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Wyświetlenie pustego przycisku, a następnie komunikatu na nim.'''
        self.screen.fill(self.button_color, self.rect)  # Wyświetlamy prostokąt przedstawiający przycisk
        self.screen.blit(self.msg_image, self.msg_image_rect)  # Wyświetlenie obrazu tekstu na ekranie