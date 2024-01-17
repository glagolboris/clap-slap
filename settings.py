import pygame


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

class EditNicknames(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/buttons/edit_nicknames.png')
        self.rect = self.image.get_rect()
        self.rect.y += 225
        self.rect.x += 150

class Settings:
    window = 1

    def __init__(self, music_, sounds_):
        self.music_ = music_
        self.sounds_ = sounds_

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

        pygame.display.flip()
