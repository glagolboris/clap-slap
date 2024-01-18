import pygame
import game

class BackToMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/menu.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 50
        self.image = pygame.transform.scale(self.image, (100, 100))

class Main:
    def __init__(self, scores, l_nick, r_nick):
        self.scores = scores
        self.l_nick = l_nick
        self.r_nick = r_nick
        self.sprites = pygame.sprite.Group()

        menu = BackToMenu()
        self.sprites.add(menu)
        self.sprites.update()

        self.font = pygame.font.Font('data/Sriracha.ttf', 36)





    def render(self, screen):
        screen.fill("#EDD834")
        if self.scores[game.Game.LEFT_PLAYER] > self.scores[game.Game.RIGHT_PLAYER]:
            nick = self.l_nick

        else:
            nick = self.r_nick


        text_blit = self.font.render(f"Победитель - {nick}. Поздравляем!", False, (0, 0, 0))
        text_blit2 = self.font.render(f"Счёт - {self.scores[game.Game.LEFT_PLAYER]} : {self.scores[game.Game.RIGHT_PLAYER]}", False, (0, 0, 0))

        screen.blit(text_blit, (40, 150))
        screen.blit(text_blit2, (250, 200))

        self.sprites.draw(screen)
        pygame.display.flip()


