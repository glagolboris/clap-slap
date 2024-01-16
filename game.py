import pygame
import random
import audio


class Pause(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/pause.png')
        self.rect = self.image.get_rect()
        self.rect.x += 324
        self.rect.y += 10
        self.image = pygame.transform.scale(self.image, (50, 50))


class Buttons:
    pass


class Continue(Buttons, pygame.sprite.Sprite):
    def __init__(self):
        super(Continue, self).__init__()
        self.image = pygame.image.load('data/buttons/continue.png')
        self.rect = self.image.get_rect()
        self.rect.y += 100
        self.rect.x += 150


class ToMenu(Buttons, pygame.sprite.Sprite):
    def __init__(self):
        super(ToMenu, self).__init__()
        self.image = pygame.image.load('data/buttons/to_menu.png')
        self.rect = self.image.get_rect()
        self.rect.y += 200
        self.rect.x += 150


class PauseMenu(pygame.sprite.Sprite):
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        continue_bttn = Continue()
        to_menu = ToMenu()
        self.all_sprites.add(continue_bttn)
        self.all_sprites.add(to_menu)
        self.all_sprites.update()

    def menu_render(self, screen):
        overlay_surface = pygame.Surface((700, 700), pygame.SRCALPHA)
        overlay_surface.fill((0, 0, 0, 128))
        screen.blit(overlay_surface, (0, 0))
        self.all_sprites.draw(screen)
        pygame.display.flip()


class Cross(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/cross.png')
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.image, (20, 20))


class Shackles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/shackles.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (465, 265))


class Fake_Defends:
    def __init__(self):
        self.cross_sprites = pygame.sprite.Group()
        self.cross = Cross()
        self.cross_sprites.add(self.cross)

        self.shackles_sprites = pygame.sprite.Group()
        self.shackles = Shackles()
        self.shackles_sprites.add(self.shackles)

    def render(self, game, screen):
        if game.FAKE_DEFENDS <= 3:
            self.cross.rect.y = 60

            if game.players['fighter'] == game.RIGHT_PLAYER:
                self.cross.rect.x = 45
                for i in range(game.FAKE_DEFENDS):
                    self.cross.rect.x += 25
                    self.cross_sprites.update()
                    self.cross_sprites.draw(screen)
                    pygame.display.flip()


            elif game.players['fighter'] == game.LEFT_PLAYER:
                self.cross.rect.x = 500
                for i in range(game.FAKE_DEFENDS):
                    self.cross.rect.x += 25
                    self.cross_sprites.update()
                    self.cross_sprites.draw(screen)
                    pygame.display.flip()

        if game.FAKE_DEFENDS >= 3:
            audio.Bell().play()
            self.shackles_render(game, screen)

    def shackles_render(self, game, screen):
        self.shackles.rect.y = 255
        if game.players['fighter'] == game.RIGHT_PLAYER:
            self.shackles.rect.x = -160


        elif game.players['fighter'] == game.LEFT_PLAYER:
            self.shackles.rect.x = 600

        self.shackles_sprites.update()
        self.shackles_sprites.draw(screen)
        pygame.display.flip()

class OnRoll(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/on_a_roll.png')
        self.rect = self.image.get_rect()

class Roll:
    def __init__(self):
        self.roll_group = pygame.sprite.Group()

        self.roll = OnRoll()
        self.roll_group.add(self.roll)

    def render(self, game, screen):
        print(True)
        self.roll.rect.y = 150

        if game.players['fighter'] == game.LEFT_PLAYER:
            self.roll.rect.x = 30

        elif game.players['fighter'] == game.RIGHT_PLAYER:
            self.roll.rect.x = 370

        self.roll_group.update()
        self.roll_group.draw(screen)
        pygame.display.flip()

class Game:
    LEFT_PLAYER = 'left_player'
    RIGHT_PLAYER = 'right_player'

    def __init__(self):
        self.reset()

        from hands import Hands
        self.hands = Hands()

        self.all_sprites = pygame.sprite.Group()

        pause = Pause()
        self.all_sprites.add(pause)

    def reset(self, menu=None):
        self.players = {'fighter': None}
        self.SCORES = {self.LEFT_PLAYER: 0, self.RIGHT_PLAYER: 0}
        self.PAUSED = False
        self.FAKE_DEFENDS = 0
        self.TRUE_ATTACKS = 0

        if menu:
            menu.GAME_STARTED = False
            menu.SETTINGS_STARTED = False
            menu.TO_MENU = True

    def sprites_render(self, screen):
        self.all_sprites.update()
        self.all_sprites.draw(screen)

    def fighter_defender(self, screen, attack_change):
        self.sprites_render(screen)
        if not self.players['fighter']:
            fighter = random.randint(1, 2)
            if fighter == 1:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
                self.players['fighter'] = self.LEFT_PLAYER
                self.sprites_render(screen)
                self.hands.all_sprites_l.draw(screen)
                self.hands.all_sprites_r.draw(screen)

            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                self.players['fighter'] = self.RIGHT_PLAYER
                self.sprites_render(screen)
                self.hands.all_sprites_r.draw(screen)
                self.hands.all_sprites_l.draw(screen)

        else:
            if self.players['fighter'] == self.LEFT_PLAYER:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)

                if attack_change:
                    pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                    pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                    self.players['fighter'] = self.RIGHT_PLAYER
                    self.sprites_render(screen)
                    self.hands.all_sprites_r.draw(screen)
                    self.hands.all_sprites_l.draw(screen)

                else:
                    self.players['fighter'] = self.LEFT_PLAYER
                    self.sprites_render(screen)
                    self.hands.all_sprites_l.draw(screen)
                    self.hands.all_sprites_r.draw(screen)
            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                if attack_change:
                    pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                    pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
                    self.players['fighter'] = self.LEFT_PLAYER
                    self.sprites_render(screen)
                    self.hands.all_sprites_l.draw(screen)
                    self.hands.all_sprites_r.draw(screen)

                else:
                    self.players['fighter'] = self.RIGHT_PLAYER
                    self.sprites_render(screen)
                    self.hands.all_sprites_r.draw(screen)
                    self.hands.all_sprites_l.draw(screen)

    def render(self, screen, attack_change=True, game=None):
        screen.fill(pygame.Color('black'))
        self.fighter_defender(screen, attack_change)

        if game:
            self.if_game(game, screen)

    def if_game(self, game, screen):
        if game.TRUE_ATTACKS >= 3:
            Roll().render(game, screen)