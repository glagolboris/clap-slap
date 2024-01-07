import pygame
import random
from menu import MainMenu as menu_mainMenu
from menu import Settings as menu_settings
from menu import Start as menu_start


class Game:
    players = {'fighter': None}
    LEFT_PLAYER = 'left_player'
    RIGHT_PLAYER = 'right_player'

    def __init__(self):
        from hands import Hands
        self.hands = Hands()


    def fighter_defender(self):
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
        self.fighter_defender()
        self.hands.all_sprites.update()

        if self.players['fighter'] == self.LEFT_PLAYER:
            self.hands.left_hand.build()
            self.hands.right_hand.build()

        if self.players['fighter'] == self.RIGHT_PLAYER:
            self.hands.right_hand.build()
            self.hands.left_hand.build()

        self.hands.all_sprites.draw(screen)
