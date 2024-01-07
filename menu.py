import pygame

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/logo.png')
        self.rect = self.image.get_rect()
        self.rect.y += -100
        self.rect.x += 50
        self.image = pygame.transform.scale(self.image, (600, 400))


class Buttons:
    pass

class Start(Buttons, pygame.sprite.Sprite):
    def __init__(self):
        super(Start, self).__init__()
        self.image = pygame.image.load('data/buttons/start.png')
        self.rect = self.image.get_rect()
        self.rect.y += 300
        self.rect.x += 150


class MainMenu:
    GAME_STARTED = False

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

        logo = Logo()
        self.all_sprites.add(logo)

        start_bttn = Start()
        self.all_sprites.add(start_bttn)




    def render(self, screen):
        screen.fill(pygame.Color('#7D1424'))
        self.all_sprites.update()
        self.all_sprites.draw(screen)

