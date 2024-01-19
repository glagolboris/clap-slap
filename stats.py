import pygame
import game


class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/statistic.png')
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


class Next(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/next_page.png')
        self.rect = self.image.get_rect()
        self.rect.y += 550
        self.rect.x += 550


class Previous(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/previous_page.png')
        self.rect = self.image.get_rect()
        self.rect.y += 550
        self.rect.x += 25


class Reset(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/clear.png')
        self.rect = self.image.get_rect()
        self.rect.y += 550
        self.rect.x += 310


class Main:
    def __init__(self, database):
        self.next_page = False
        self.previous_page = False
        self.clearing = False
        self.database = database
        self.sprites = pygame.sprite.Group()
        self.next = pygame.sprite.Group()
        self.previous = pygame.sprite.Group()
        self.reset = pygame.sprite.Group()

        menu = Back()
        self.sprites.add(menu)

        logo = Logo()
        self.sprites.add(logo)

        next = Next()
        self.next.add(next)

        previous = Previous()
        self.previous.add(previous)

        clear = Reset()

        self.reset.add(clear)
        self.reset.update()
        self.next.update()
        self.previous.update()
        self.sprites.update()

        self.font = pygame.font.Font('data/Sriracha.ttf', 40)
        self.page = 1

    def render(self, screen):
        self.next_page = False
        self.previous_page = False
        self.clearing = False

        screen.fill("#7D1424")

        place = 125
        for stat_elem in self.database.get_page(self.page):
            text_blit = self.font.render(f"{stat_elem[0]} - {stat_elem[1]}. {str(stat_elem[2])}:{str(stat_elem[3])}",
                                         False, (255, 252, 230))
            screen.blit(text_blit, (100, place))
            place += 50

        pages = self.database.pages_count()
        if pages >= 1 and self.page != pages:
            self.next_page = True
            self.next.draw(screen)

        if pages >= 1 and self.page != 1:
            self.previous_page = True
            self.previous.draw(screen)

        if pages > 0:
            self.clearing = True
            self.reset.draw(screen)

        self.sprites.draw(screen)
        pygame.display.flip()
