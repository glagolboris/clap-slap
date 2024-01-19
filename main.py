import time
import pygame
from menu import MainMenu as menu_mainMenu
from menu import Settings as menu_settings
from menu import Start as menu_start
from menu import Exit as menu_exit
from menu import Statisitc as menu_stat
from settings import Back
from settings import Settings
import settings
from game import Pause, Continue, ToMenu, Score
from game import Game
from game import PauseMenu
import audio
from audio import Music, Sounds
from db import Base
import winner_window
from winner_window import Main as winner_w
import stats

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

database = Base()

from game import Fake_Defends

fd = Fake_Defends()

from game import Roll

roll = Roll()
pygame.display.flip()
last_key_time = 0
key_delay = 150
current_keys = set()

audio_lab = audio.Main()

box_typer = False

stat = stats.Main(database=database)


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
                if game.TRUE_ATTACKS >= 3:
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
    clock.tick(100)
    events = pygame.event.get()
    for event in events:
        if menu.GAME_STARTED:
            if event.type == pygame.QUIT:
                running = False

            if not game.PAUSED:
                if event.type == pygame.MOUSEBUTTONUP:
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
            if sett.window == 1:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Back().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            menu.SETTINGS_STARTED = False
                            menu.TO_MENU = True
                            menu.render(screen)

                        if settings.SoundMenu().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            sett.window = 2
                            sett.render(screen)

                        if settings.EditNicknames().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            sett.window = 3
                            sett.render(screen)

            elif sett.window == 2:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
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

            elif sett.window == 3:
                box_typer = True
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if Back().rect.collidepoint(event.pos):
                            box_typer = False
                            sounds.clicked.play()
                            sett.window = 1
                            screen.fill('black')
                            sett.render(screen)
                            pygame.display.flip()

                        elif settings.ResetButton().rect.collidepoint(event.pos):
                            sounds.clicked.play()
                            database.edit_ln('Игрок 1')
                            database.edit_rn('Игрок 2')
                            sett.box_1.text = database.get_ln()
                            sett.box_2.text = database.get_rn()
                            sett.render(screen)

                if box_typer:
                    for box in sett.boxes:
                        box.handle_event(event, db_=database)
                        box.update()
                        box.draw(screen)
                        pygame.display.flip()

        if menu.WINNER_WINDOW:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if winner_window.BackToMenu().rect.collidepoint(event.pos):
                        sounds.clicked.play()
                        menu.WINNER_WINDOW = False
                        menu.TO_MENU = True
                        music.winner.stop()
                        music.menu.play()
                        game.reset(menu=menu)
                        menu.render(screen)

        if menu.STATISTIC:
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if stats.Back().rect.collidepoint(event.pos):
                        sounds.clicked.play()
                        menu.STATISTIC = False
                        menu.TO_MENU = True
                        menu.render(screen)

                    if stats.Next().rect.collidepoint(event.pos):
                        if stat.next_page == True:
                            sounds.clicked.play()
                            stat.page += 1
                            stat.render(screen)

                    if stats.Previous().rect.collidepoint(event.pos):
                        if stat.previous_page == True:
                            sounds.clicked.play()
                            stat.page -= 1
                            stat.render(screen)

                    if stats.Reset().rect.collidepoint(event.pos):
                        if stat.clearing == True:
                            sounds.clicked.play()
                            database.delete_scores()
                            stat.render(screen)

                    if stats.Previous().rect.collidepoint(event.pos):
                        if stat.previous_page == True:
                            sounds.clicked.play()
                            stat.page -= 1
                            stat.render(screen)

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

                    if menu_stat().rect.collidepoint(event.pos):
                        sounds.clicked.play()
                        menu.TO_MENU = False
                        menu.STATISTIC = True
                        stat.page = 1
                        stat.render(screen)

        clock.tick(60)
        pygame.display.flip()

    if box_typer:
        for box in sett.boxes:
            box.update()
            box.draw(screen)
            pygame.display.flip()

        sett.render(screen)

        for box in sett.boxes:
            box.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    if menu.GAME_STARTED and not game.PAUSED:
        if game.SCORES[game.LEFT_PLAYER] < 10 and game.SCORES[game.RIGHT_PLAYER] < 10:
            process_keys(events)

        else:
            menu.GAME_STARTED = False
            menu.WINNER_WINDOW = True
            database.add_score(database.get_ln(), database.get_rn(), game.SCORES[game.LEFT_PLAYER],
                               game.SCORES[game.RIGHT_PLAYER])
            music.game.stop()
            music.winner.play()
            winner_w(game.SCORES, database.get_ln(), database.get_rn()).render(screen)
