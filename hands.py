import pygame
from game import Game
import audio
import game as gm

clock = pygame.time.Clock()


class Hands:
    def __init__(self):
        self.all_sprites_l = pygame.sprite.Group()
        self.all_sprites_r = pygame.sprite.Group()
        self.left_hand = LeftHand()
        self.right_hand = RightHand()
        self.all_sprites_l.add(self.left_hand)
        self.all_sprites_r.add(self.right_hand)

    def render(self, screen, role):
        self.all_sprites_l.update()
        screen.fill('black')

        if role == 'left_player':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
        elif role == 'right_player':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)

        self.all_sprites_r.draw(screen)
        self.all_sprites_l.draw(screen)
        Game().sprites_render(screen)


        pygame.display.flip()
        clock.tick(60)

    def attack_and_defend(self, screen, who_attacked, game=None):
        if who_attacked == 'left_player':
            audio.Woosh2().play()
            for _ in range(10):
                self.left_hand.rect.x += 21
                self.right_hand.rect.x += 21
                self.render(screen, role=who_attacked)
                if game:
                    Game().if_game(game, screen)

            for __ in range(10):
                self.left_hand.rect.x -= 21
                self.right_hand.rect.x -= 21
                self.render(screen, role=who_attacked)
                if game:
                    Game().if_game(game, screen)

        if who_attacked == 'right_player':
            audio.Woosh2().play()
            for _ in range(10):
                self.left_hand.rect.x -= 21
                self.right_hand.rect.x -= 21
                self.render(screen, role=who_attacked)
                if game:
                    Game().if_game(game, screen)


            for __ in range(10):
                self.left_hand.rect.x += 21
                self.right_hand.rect.x += 21
                self.render(screen, role=who_attacked)
                if game:
                    Game().if_game(game, screen)


class LeftHand(pygame.sprite.Sprite, Hands):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (600, 400))
        self.rect.x = -210
        self.rect.y = 190

    def render(self, screen, hands, role, game=None):
        hands.all_sprites_l.update()
        screen.fill('black')

        if role == 'attack':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
        elif role == 'defend':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)

        hands.all_sprites_r.draw(screen)
        hands.all_sprites_l.draw(screen)
        Game().sprites_render(screen)

        if game:
            Game().if_game(game, screen)

        pygame.display.flip()
        clock.tick(60)

    def attack(self, hands, screen, game=None):
        audio.Slap().play()
        for _ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='attack', game=game)

        for __ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='attack', game=game)

    def defend(self, hands, screen, game=None):
        audio.Woosh1().play()
        for _ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='defend', game=game)

        for __ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='defend', game=game)


class RightHand(pygame.sprite.Sprite, Hands):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (600, 400))
        self.rect.x = 310
        self.rect.y = 170
        self.attackCount = 10

    def render(self, screen, hands, role, game=None):
        hands.all_sprites_r.update()
        screen.fill('black')
        if role == 'attack':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
        elif role == 'defend':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
        hands.all_sprites_l.draw(screen)
        hands.all_sprites_r.draw(screen)
        Game().sprites_render(screen)

        if game:
            Game().if_game(game, screen)

        pygame.display.flip()
        clock.tick(60)

    def attack(self, hands, screen, game=None):
        audio.Slap().play()

        for _ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='attack', game=game)


        for __ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='attack', game=game)

    def defend(self, hands, screen, game=None):
        audio.Woosh1().play()
        for _ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='defend', game=game)

        for __ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='defend', game=game)
