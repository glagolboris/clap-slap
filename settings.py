import pygame

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/settings_logo.png')
        self.rect = self.image.get_rect()
        self.rect.y += 10
        self.rect.x += 150

class Back(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/back.png')
        self.rect = self.image.get_rect()
        self.rect.y += 1
        self.rect.x += 600


class Settings:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

        logo = Logo()
        self.all_sprites.add(logo)

        back = Back()
        self.all_sprites.add(back)

    def render(self, screen):
        screen.fill(pygame.Color('#7D1424'))
        self.all_sprites.update()
        self.all_sprites.draw(screen)

