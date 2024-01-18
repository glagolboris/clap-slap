import pygame
from db import Base as database

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/settings_logo.png')
        self.rect = self.image.get_rect()
        self.rect.y += 10
        self.rect.x += 150


class Back(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/back.png')
        self.rect = self.image.get_rect()
        self.rect.y += 1
        self.rect.x += 600

class SoundMenu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/buttons/sound_sett.png')
        self.rect = self.image.get_rect()
        self.rect.y += 125
        self.rect.x += 150

class Music(pygame.sprite.Sprite):
    def __init__(self, music):
        pygame.sprite.Sprite.__init__(self)
        if music.volume:
            self.image = pygame.image.load('data/buttons/sett_music_off.png')

        else:
            self.image = pygame.image.load('data/buttons/sett_music_on.png')

        self.rect = self.image.get_rect()
        self.rect.y += 125
        self.rect.x += 150


class Sounds(pygame.sprite.Sprite):
    def __init__(self, music):
        pygame.sprite.Sprite.__init__(self)
        if music.volume:
            self.image = pygame.image.load('data/buttons/sett_sounds_off.png')

        else:
            self.image = pygame.image.load('data/buttons/sett_sounds_on.png')

        self.rect = self.image.get_rect()
        self.rect.y += 225
        self.rect.x += 150

class InputBox:
    pygame.init()
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('dodgerblue2')
    FONT = pygame.font.SysFont('Comic Sans MS', 48)

    def __init__(self, x, y, w, h, text='', player=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.player = player

    def handle_event(self, event, db_=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                if self.player == 1:
                    db_.edit_ln(self.text)

                elif self.player == 2:
                    db_.edit_rn(self.text)

                self.active = False

            self.txt_surface = self.FONT.render(self.text, True, self.color)

            if db_ and self.player == 1:
                db_.edit_ln(self.text)

            elif db_ and self.player == 2:
                db_.edit_rn(self.text)

            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if db_ and self.player == 1:
                        db_.edit_ln(self.text)

                    elif db_ and self.player == 2:
                        db_.edit_rn(self.text)

                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.FONT.render(self.text, True, self.color)



    def update(self, player=None, db_=None):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        if player and db_:
            if player == 1:
                self.text = db_.get_ln()

            elif player == 2:
                self.text = db_.get_rn()

    def draw(self, screen):
        screen.blit(self.FONT.render(self.text, True, self.color), (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


class EditNicknames(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/buttons/edit_nicknames.png')
        self.rect = self.image.get_rect()
        self.rect.y += 225
        self.rect.x += 150

class Player1_Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/player_1.png')
        self.rect = self.image.get_rect()
        self.rect.x += 10
        self.rect.y += 190

class Player2_Logo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/player_2.png')
        self.rect = self.image.get_rect()
        self.rect.x += 10
        self.rect.y += 390

class ResetButton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/reset.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 550
        self.image = pygame.transform.scale(self.image, (100, 100))

class Settings:
    window = 1

    def __init__(self, music_, sounds_):
        self.music_ = music_
        self.sounds_ = sounds_
        self.database = database()
        self.box_1 = InputBox(350, 200, 140, 75, text=self.database.get_ln(), player=1)
        self.box_2 = InputBox(350, 400, 140, 75, text=self.database.get_rn(), player=2)
        self.boxes = [self.box_1, self.box_2]


    def sprites_init(self):
        self.window_1 = pygame.sprite.Group()
        self.window_2 = pygame.sprite.Group()
        self.window_3 = pygame.sprite.Group()

        logo = Logo()
        self.window_1.add(logo)
        self.window_2.add(logo)
        self.window_3.add(logo)

        back = Back()
        self.window_1.add(back)
        self.window_2.add(back)
        self.window_3.add(back)

        edit_nicknames = EditNicknames()
        self.window_1.add(edit_nicknames)

        sound_menu = SoundMenu()
        self.window_1.add(sound_menu)

        sounds = Sounds(music=self.sounds_)
        music = Music(music=self.music_)
        self.window_2.add(sounds)
        self.window_2.add(music)

        player_1 = Player1_Logo()
        player_2 = Player2_Logo()
        reset = ResetButton()
        self.window_3.add(player_1)
        self.window_3.add(player_2)
        self.window_3.add(reset)


    def render(self, screen):
        screen.fill(pygame.Color('#7D1424'))
        self.sprites_init()

        if self.window == 1:
            self.window_1.update()
            self.window_1.draw(screen)

        elif self.window == 2:
            self.window_2.update()
            self.window_2.draw(screen)

        elif self.window == 3:
            self.window_3.update()
            self.window_3.draw(screen)

            for box in self.boxes:
                box.update()
                box.draw(screen)


