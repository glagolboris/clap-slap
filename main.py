import pygame
from menu import MainMenu as menu_mainMenu
from menu import Settings as menu_settings
from menu import Start as menu_start
from settings import Back
from game import Pause, Continue, ToMenu
from game import Game
from game import PauseMenu
import audio

pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
from hands import Hands
game = Game()
hands = Hands()
menu = menu_mainMenu()

from game import Fake_Defends
fd = Fake_Defends()
# game.render(screen)
pygame.display.flip()
last_key_time = 0
key_delay = 150
current_keys = set()

audio_lab = audio.Main()


def process_keys(events):
    global current_keys
    global last_key_time
    global current_keys
    current_time = pygame.time.get_ticks()

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                current_keys.add(event.key)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                current_keys.discard(event.key)

    if current_time - last_key_time >= key_delay:
        if pygame.K_LSHIFT in current_keys and pygame.K_RSHIFT in current_keys:
            game.FAKE_DEFENDS = 0
            game.TRUE_ATTACKS = 0
            hands.attack_and_defend(screen, game.players['fighter'])
            game.render(screen)



        elif pygame.K_RSHIFT in current_keys:
            if game.players['fighter'] == game.RIGHT_PLAYER:
                hands.right_hand.attack(hands, screen)
                if game.TRUE_ATTACKS == 3:
                    game.SCORES[game.RIGHT_PLAYER] += 2

                else:
                    game.TRUE_ATTACKS += 1
                    game.SCORES[game.RIGHT_PLAYER] += 1

                game.FAKE_DEFENDS = 0

            else:
                if game.FAKE_DEFENDS < 3:
                    hands.right_hand.defend(hands, screen)
                    game.FAKE_DEFENDS += 1
                    fd.render(game, screen)


        elif pygame.K_LSHIFT in current_keys:
            if game.players['fighter'] == game.LEFT_PLAYER:
                hands.left_hand.attack(hands, screen)
                if game.TRUE_ATTACKS == 3:
                    game.SCORES[game.LEFT_PLAYER] += 2

                else:
                    game.TRUE_ATTACKS += 1
                    game.SCORES[game.LEFT_PLAYER] += 1

                game.FAKE_DEFENDS = 0

            else:
                if game.FAKE_DEFENDS < 3:
                    hands.left_hand.defend(hands, screen)
                    game.FAKE_DEFENDS += 1
                    fd.render(game, screen)



        last_key_time = current_time

while running:
    events = pygame.event.get()
    for event in events:
        if menu.GAME_STARTED:
            if event.type == pygame.QUIT:
                running = False

            if not game.PAUSED:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Pause().rect.collidepoint(event.pos):
                            audio.Game().stop()
                            audio.Clicked().play()
                            game.PAUSED = True
                            PauseMenu().menu_render(screen)

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Continue().rect.collidepoint(event.pos):
                            audio.Clicked().play()
                            audio.Game().play()
                            game.PAUSED = False
                            screen.fill('black')
                            game.render(screen, attack_change=False)
                            pygame.display.flip()

                        if ToMenu().rect.collidepoint(event.pos):
                            audio.Clicked().play()
                            audio.Menu().play()
                            menu.GAME_STARTED = False
                            game.PAUSED = False
                            game.players['fighter'] = None
                            game.SCORES = {game.LEFT_PLAYER: 0, game.RIGHT_PLAYER: 0}
                            menu.TO_MENU = True
                            screen.fill('black')





        elif menu.SETTINGS_STARTED:

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Back().rect.collidepoint(event.pos):
                        audio.Clicked().play()
                        menu.SETTINGS_STARTED = False
                        menu.TO_MENU = True
                        menu.render(screen)
        if menu.TO_MENU:
            if not audio_lab.MUSIC_PLAYED:
                audio.Menu().play()
                audio_lab.MUSIC_PLAYED = True
            menu.render(screen)
            pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_start().rect.collidepoint(event.pos):
                        audio.Clicked().play()
                        menu.GAME_STARTED = True
                        menu.TO_MENU = False
                        game.render(screen)
                        audio.Menu().stop()
                        audio.Game().play()
                    if menu_settings().rect.collidepoint(event.pos):
                        audio.Clicked().play()
                        import settings
                        settings.Settings().render(screen)
                        menu.SETTINGS_STARTED = True
                        menu.TO_MENU = False

        clock.tick(60)
        pygame.display.flip()

    if menu.GAME_STARTED and not game.PAUSED:
        if game.SCORES[game.LEFT_PLAYER] < 10 and game.SCORES[game.RIGHT_PLAYER] < 10:
            process_keys(events)
            print(game.SCORES)

        else:
            game.reset(menu)
            audio.Game().stop()
            audio.Menu().play()



