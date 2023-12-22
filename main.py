import pygame
import random


class Game:
    players = {'fighter': None}

    def __init__(self):
        pass

    def render(self, screen):
        screen.fill(pygame.Color('black'))
        if not self.players['fighter']:
            fighter = random.randint(1, 2)
            if fighter == 1:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)

            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)

            self.players['fighter'] = fighter

        else:
            if self.players['fighter'] == 1:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
                self.players['fighter'] = 2


            else:
                pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
                pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
                self.players['fighter'] = 1


if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True

    game = Game()
    game.render(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.render(screen)
            clock.tick(60)
            pygame.display.flip()
