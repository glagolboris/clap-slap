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


    def render(self, screen, role):
        self.all_sprites_l.update()
        screen.fill('black')

        if role == 'left_player':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
        elif role == 'right_player':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)

        self.all_sprites_r.draw(screen)
        self.all_sprites_l.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    def attack_and_defend(self, screen, who_attacked):
        if who_attacked == 'left_player':
            for _ in range(10):
                self.left_hand.rect.x += 21
                self.right_hand.rect.x += 21
                self.render(screen, role=who_attacked)

            for __ in range(10):
                self.left_hand.rect.x -= 21
                self.right_hand.rect.x -= 21
                self.render(screen, role=who_attacked)

        if who_attacked == 'right_player':
            for _ in range(10):
                self.left_hand.rect.x -= 21
                self.right_hand.rect.x -= 21
                self.render(screen, role=who_attacked)

            for __ in range(10):
                self.left_hand.rect.x += 21
                self.right_hand.rect.x += 21
                self.render(screen, role=who_attacked)









class LeftHand(pygame.sprite.Sprite, Hands):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (600, 400))
        self.rect.x = -210
        self.rect.y = 190

    def render(self, screen, hands, role):
        hands.all_sprites_l.update()
        screen.fill('black')

        if role == 'attack':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
        elif role == 'defend':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)

        hands.all_sprites_r.draw(screen)
        hands.all_sprites_l.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    def attack(self, hands, screen):
        for _ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='attack')

        for __ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='attack')

    def defend(self, hands, screen):
        for _ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='defend')

        for __ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='defend')


class RightHand(pygame.sprite.Sprite, Hands):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hand.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (600, 400))
        self.rect.x = 310
        self.rect.y = 170
        self.attackCount = 10

    def render(self, screen, hands, role):
        hands.all_sprites_r.update()
        screen.fill('black')
        if role == 'attack':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (350, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (0, 0, 350, 700), 350)
        elif role == 'defend':
            pygame.draw.rect(screen, pygame.Color('#F24D16'), (0, 0, 350, 700), 350)
            pygame.draw.rect(screen, pygame.Color('#4CD4B0'), (350, 0, 350, 700), 350)
        hands.all_sprites_l.draw(screen)
        hands.all_sprites_r.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    def attack(self, hands, screen):
        for _ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='attack')


        for __ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='attack')


    def defend(self, hands, screen):
        for _ in range(10):
            self.rect.x -= 21
            self.render(screen, hands, role='defend')

        for __ in range(10):
            self.rect.x += 21
            self.render(screen, hands, role='defend')


