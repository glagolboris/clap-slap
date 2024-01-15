import pygame

clock = pygame.time.Clock()


class Hands:
    def __init__(self):
        self.all_sprites_l = pygame.sprite.Group()
        self.all_sprites_r = pygame.sprite.Group()
        self.left_hand = LeftHand()
        self.right_hand = RightHand()
        self.all_sprites_l.add(self.left_hand)
        self.all_sprites_r.add(self.right_hand)


class LeftHand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (600, 400))
        self.rect.x = -210
        self.rect.y = 190

    def attack(self, screen):
        for i in range(5):
            if i < 2:
                self.rect.x += 105
            elif i > 2:
                self.rect.x -= 105


class RightHand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (600, 400))
        self.rect.x = 310
        self.rect.y = 170
        self.attackCount = 10

    def attack(self, Is, hands, screen):
        if Is:
            if self.attackCount > 0:
                    self.rect.x -= 21
                    self.attackCount -= 1
            elif self.attackCount < 0:
                    self.rect.x += 21
                    self.attackCount -= 1
            else:
                self.attackCount -= 1
            print(self.attackCount)
            print(self.rect.x)
        else:
            self.attackCount = 10
        hands.all_sprites_r.update()
        hands.all_sprites_r.draw(screen)
        pygame.display.flip()


    def attackIs(self):
        return self.attackCount
