import pygame
from menu import MainMenu as menu_mainMenu
from menu import Settings as menu_settings
from menu import Start as menu_start
from menu import Exit as menu_exit
from settings import Back
from settings import Settings
import settings
from game import Pause, Continue, ToMenu, Score
from game import Game
from game import PauseMenu
import audio
from audio import Music, Sounds

pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
from hands import Hands

sounds = Sounds()
music = Music()

game = Game()
hands = Hands()
menu = menu_mainMenu()
sett = Settings(sounds_=sounds, music_=music)



from game import Fake_Defends
fd = Fake_Defends()

from game import Roll
roll = Roll()
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
            if game.FAKE_DEFENDS < 3:
                game.FAKE_DEFENDS = 0
                game.TRUE_ATTACKS = 0
                hands.attack_and_defend(screen, game.players['fighter'], sounds=sounds)
                game.render(screen, game=game)

            else:
                if game.players['fighter'] == game.RIGHT_PLAYER:
                    hands.right_hand.attack(hands, screen, game=game, sounds=sounds)
                    if game.TRUE_ATTACKS >= 3:
                        roll.render(game, screen)
                        game.SCORES[game.RIGHT_PLAYER] += 2
                        game.TRUE_ATTACKS += 1


                    else:
                        game.TRUE_ATTACKS += 1
                        game.SCORES[game.RIGHT_PLAYER] += 1

                    game.FAKE_DEFENDS = 0
                    Score().render(game, screen)

                if game.players['fighter'] == game.LEFT_PLAYER:
                    hands.left_hand.attack(hands, screen, game=game, sounds=sounds)
                    if game.TRUE_ATTACKS >= 3:
                        game.SCORES[game.LEFT_PLAYER] += 2
                        game.TRUE_ATTACKS += 1

                    else:
                        game.TRUE_ATTACKS += 1
                        game.SCORES[game.LEFT_PLAYER] += 1

                    Score().render(game, screen)

            Score().render(game, screen)




        elif pygame.K_RSHIFT in current_keys:
            if game.players['fighter'] == game.RIGHT_PLAYER:
                hands.right_hand.attack(hands, screen, game=game, sounds=sounds)
                if game.TRUE_ATTACKS == 3:
                    game.SCORES[game.RIGHT_PLAYER] += 2
                    game.TRUE_ATTACKS += 1

                else:
                    game.TRUE_ATTACKS += 1
                    game.SCORES[game.RIGHT_PLAYER] += 1

                game.FAKE_DEFENDS = 0

                if game.TRUE_ATTACKS == 3:
                    roll.render(game, screen)
                    sounds.bang.play()

            else:
                if game.FAKE_DEFENDS < 3:
                    hands.right_hand.defend(hands, screen, game=game, sounds=sounds)
                    game.FAKE_DEFENDS += 1
                    fd.render(game, screen, sounds)

            Score().render(game, screen)


        elif pygame.K_LSHIFT in current_keys:
            if game.players['fighter'] == game.LEFT_PLAYER:
                hands.left_hand.attack(hands, screen, game=game, sounds=sounds)
                if game.TRUE_ATTACKS >= 3:
                    game.SCORES[game.LEFT_PLAYER] += 2
                    game.TRUE_ATTACKS += 1

                else:
                    game.TRUE_ATTACKS += 1
                    game.SCORES[game.LEFT_PLAYER] += 1

                game.FAKE_DEFENDS = 0

                if game.TRUE_ATTACKS == 3:
                    roll.render(game, screen)
                    sounds.bang.play()

            else:
                if game.FAKE_DEFENDS < 3:
                    hands.left_hand.defend(hands, screen, game=game, sounds=sounds)
                    game.FAKE_DEFENDS += 1
                    fd.render(game, screen, sounds)

            Score().render(game, screen)

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
                            music.game.stop()
                            sounds.clicked.play()
                            game.PAUSED = True
                            PauseMenu().menu_render(screen)

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Continue().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            music.game.play()
                            game.PAUSED = False
                            screen.fill('black')
                            game.render(screen, attack_change=False, game=game)
                            if game.FAKE_DEFENDS >= 3:
                                fd.render(game, screen, sounds)
                            pygame.display.flip()

                        if ToMenu().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            music.menu.play()
                            menu.GAME_STARTED = False
                            game.reset(menu)
                            menu.TO_MENU = True
                            screen.fill('black')





        elif menu.SETTINGS_STARTED:

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if sett.window == 1:
                        if Back().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            menu.SETTINGS_STARTED = False
                            menu.TO_MENU = True
                            menu.render(screen)

                        if settings.SoundMenu().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            sett.window = 2
                            sett.render(screen)

                    elif sett.window == 2:
                        if Back().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            sett.window = 1
                            sett.render(screen)

                        if settings.Music(music).rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            music.volume = not music.volume
                            if not music.volume:
                                music.menu.stop()

                            else:
                                music.menu.play()

                            sett.render(screen)

                        if settings.Sounds(sounds).rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            sounds.volume = not sounds.volume
                            sett.render(screen)


        if menu.TO_MENU:
            if not audio_lab.MUSIC_PLAYED:
                music.menu.play()
                audio_lab.MUSIC_PLAYED = True
            menu.render(screen)
            pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_start().rect.collidepoint(event.pos):
                        sounds.clicked.play()
                        menu.GAME_STARTED = True
                        menu.TO_MENU = False
                        game.render(screen, game=game)
                        music.menu.stop()
                        music.game.play()

                    if menu_settings().rect.collidepoint(event.pos):
                        sounds.clicked.play()
                        import settings

                        sett.render(screen)
                        menu.SETTINGS_STARTED = True
                        menu.TO_MENU = False

                    if menu_exit().rect.collidepoint(event.pos):
                        sounds.clicked.play()
                        running = False

        clock.tick(60)
        pygame.display.flip()

    if menu.GAME_STARTED and not game.PAUSED:
        if game.SCORES[game.LEFT_PLAYER] < 10 and game.SCORES[game.RIGHT_PLAYER] < 10:
            process_keys(events)

        else:
            game.reset(menu)
            music.menu.stop()
            music.menu.play()
