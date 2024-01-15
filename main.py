import pygame
from menu import MainMenu as menu_mainMenu
from menu import Settings as menu_settings
from menu import Start as menu_start
from settings import Back
from game import Game

pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
from hands import Hands
game = Game()
hands = Hands()
menu = menu_mainMenu()
menu.render(screen)
# game.render(screen)
pygame.display.flip()
last_key_time = 0
key_delay = 150
current_keys = set()


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
            hands.attack_and_defend(screen, game.players['fighter'])
            game.render(screen)


        elif pygame.K_RSHIFT in current_keys:
            if game.players['fighter'] == game.RIGHT_PLAYER:
                hands.right_hand.attack(hands, screen)
                game.SCORES[game.RIGHT_PLAYER] += 1

            else:
                hands.right_hand.defend(hands, screen)

        elif pygame.K_LSHIFT in current_keys:
            if game.players['fighter'] == game.LEFT_PLAYER:
                hands.left_hand.attack(hands, screen)
                game.SCORES[game.LEFT_PLAYER] += 1

            else:
                hands.left_hand.defend(hands, screen)

        last_key_time = current_time

while running:
    events = pygame.event.get()
    for event in events:
        if menu.GAME_STARTED:
            if event.type == pygame.QUIT:
                running = False


        elif menu.SETTINGS_STARTED:
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

    if menu.GAME_STARTED:
        process_keys(events)

