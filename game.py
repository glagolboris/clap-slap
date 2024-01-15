import pygame
import random


class Game:
    players = {'fighter': None}
    LEFT_PLAYER = 'left_player'
    RIGHT_PLAYER = 'right_player'
    SCORES = {LEFT_PLAYER: 0, RIGHT_PLAYER: 0}

    def __init__(self):
        from hands import Hands
        self.hands = Hands()

    def fighter_defender(self, screen, attack_change):
        if not self.players['fighter']:
            fighter = random.randint(1, 2)
            if fighter == 1:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
                self.players['fighter'] = self.LEFT_PLAYER
                self.hands.all_sprites_l.draw(screen)
                self.hands.all_sprites_r.draw(screen)

            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                self.players['fighter'] = self.RIGHT_PLAYER
                self.hands.all_sprites_r.draw(screen)
                self.hands.all_sprites_l.draw(screen)

        else:
            if self.players['fighter'] == self.LEFT_PLAYER:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                if attack_change:
                    self.players['fighter'] = self.RIGHT_PLAYER
                    self.hands.all_sprites_r.draw(screen)
                    self.hands.all_sprites_l.draw(screen)
            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
                if attack_change:
                    self.players['fighter'] = self.LEFT_PLAYER
                    self.hands.all_sprites_l.draw(screen)
                    self.hands.all_sprites_r.draw(screen)

    def render(self, screen, attack_change=True):
        screen.fill(pygame.Color('black'))

        self.fighter_defender(screen, attack_change)


