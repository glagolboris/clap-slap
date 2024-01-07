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
hands = Hands()
menu = menu_mainMenu()
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    hands.right_hand.attack(screen)
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
