import pygame


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
        self.image = pygame.transform.scale(self.image, (500, 350))

    def build(self):
        self.rect.x = -110
        self.rect.y = 220


class RightHand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (500, 350))

    def build(self):
        self.rect.x = 310
        self.rect.y = 200
