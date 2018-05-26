import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, ai_settings):
        pygame.sprite.Sprite.__init__(self)  # Wyzwalamy sprite __init__
        self.image = pygame.image.load('images/background.png')
        self.image = pygame.transform.scale(self.image, (ai_settings.screen_width, ai_settings.screen_height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]
