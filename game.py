import pygame
import random

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
        self.rect.y += 150
        self.rect.x += 150

class ToMenu(Buttons, pygame.sprite.Sprite):
    def __init__(self):
        super(ToMenu, self).__init__()
        self.image = pygame.image.load('data/buttons/to_menu.png')
        self.rect = self.image.get_rect()
        self.rect.y += 250
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






class Game:
    players = {'fighter': None}
    LEFT_PLAYER = 'left_player'
    RIGHT_PLAYER = 'right_player'
    SCORES = {LEFT_PLAYER: 0, RIGHT_PLAYER: 0}
    PAUSED = False

    def __init__(self):
        from hands import Hands
        self.hands = Hands()

        self.all_sprites = pygame.sprite.Group()

        pause = Pause()
        self.all_sprites.add(pause)




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

    def render(self, screen, attack_change=True):
        screen.fill(pygame.Color('black'))
        self.fighter_defender(screen, attack_change)



