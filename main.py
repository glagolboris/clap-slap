import pygame
import random
from menu import MainMenu as menu_mainmenu
from menu import Settings as menu_settings
from menu import Start as menu_start
from settings import Back

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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True

    from hands import Hands

    hands = Hands()



    menu = menu_mainmenu()

    game = Game()
    menu.render(screen)
    # game.render(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if menu.GAME_STARTED:
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    game.render(screen)

                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        hands.right_hand.attack()

            if menu.SETTINGS_STARTED:
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Back().rect.collidepoint(event.pos):
                            menu.SETTINGS_STARTED = False
                            menu.render(screen)

            else:
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if menu_start().rect.collidepoint(event.pos):
                            menu.GAME_STARTED = True
                            game.render(screen)

                        if menu_settings().rect.collidepoint(event.pos):
                            import settings
                            settings.Settings().render(screen)
                            menu.SETTINGS_STARTED = True




            clock.tick(60)
            pygame.display.flip()
