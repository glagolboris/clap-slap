import pygame
import random


class Game:
    players = {'fighter': None}
    LEFT_PLAYER = 'left_player'
    RIGHT_PLAYER = 'right_player'

    def __init__(self):
        from hands import Hands
        self.hands = Hands()

    def fighter_defender(self, screen):
        if not self.players['fighter']:
            fighter = random.randint(1, 2)
            if fighter == 1:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
                self.players['fighter'] = self.LEFT_PLAYER

            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                self.players['fighter'] = self.RIGHT_PLAYER

        else:
            if self.players['fighter'] == self.LEFT_PLAYER:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                self.players['fighter'] = self.RIGHT_PLAYER
            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
                self.players['fighter'] = self.LEFT_PLAYER

    def render(self, screen):
        screen.fill(pygame.Color('black'))
        self.fighter_defender(screen)
        self.hands.all_sprites_l.update()
        self.hands.all_sprites_r.update()

        if self.players['fighter'] == self.LEFT_PLAYER:
            self.hands.all_sprites_l.draw(screen)
            self.hands.all_sprites_r.draw(screen)

        elif self.players['fighter'] == self.RIGHT_PLAYER:
            self.hands.all_sprites_r.draw(screen)
            self.hands.all_sprites_l.draw(screen)
