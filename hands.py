import pygame

clock = pygame.time.Clock()

class Hands:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.left_hand = LeftHand()
        self.right_hand = RightHand()
        self.all_sprites.add(self.left_hand)
        self.all_sprites.add(self.right_hand)


class LeftHand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (600, 400))

    def build(self):
        self.rect.x = -210
        self.rect.y = 190

    def attack(self):
        for i in range(5):
            if i < 2:
                self.rect.x += 105
            elif i > 2:
                self.rect.x -= 105
            clock.tick(60)


class RightHand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (600, 400))

    def build(self):
        self.rect.x = 310
        self.rect.y = 170

    def attack(self):
        for i in range(5):
            if i < 2:
                self.rect.x -= 105
            elif i > 2:
                self.rect.x += 105
            clock.tick(60)
        pygame.display.flip()
