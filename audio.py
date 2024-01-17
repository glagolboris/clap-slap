import pygame


class Main:
    MUSIC_PLAYED = False


class Sounds:
    volume = True
    def __init__(self):
        self.clicked = self.Clicked(self)
        self.slap = self.Slap(self)
        self.woosh_1 = self.Woosh1(self)
        self.woosh_2 = self.Woosh2(self)
        self.bell = self.Bell(self)
        self.bang = self.Bang(self)


    class Clicked:
        def __init__(self, sounds):
            self.sound = pygame.mixer.Sound("data/audio/clicked.wav")
            self.sounds = sounds

        def play(self):
            if self.sounds.volume:
                self.sound.play()

    class Slap:
        def __init__(self, sounds):
            self.sound = pygame.mixer.Sound("data/audio/slap.mp3")
            self.sounds = sounds

        def play(self):
            if self.sounds.volume:
                self.sound.play()

    class Woosh1:
        def __init__(self, sounds):
            self.sound = pygame.mixer.Sound("data/audio/woosh1.wav")
            self.sounds = sounds

        def play(self):
            if self.sounds.volume:
                self.sound.play()

    class Woosh2:
        def __init__(self, sounds):
            self.sound = pygame.mixer.Sound("data/audio/woosh2.wav")
            self.sounds = sounds

        def play(self):
            if self.sounds.volume:
                self.sound.play()

    class Bell:
        def __init__(self, sounds):
            self.sound = pygame.mixer.Sound("data/audio/bell.mp3")
            self.sounds = sounds

        def play(self):
            if self.sounds.volume:
                self.sound.play()

    class Bang:
        def __init__(self, sounds):
            self.sound = pygame.mixer.Sound("data/audio/bang.wav")
            self.sounds = sounds

        def play(self):
            if self.sounds.volume:
                self.sound.play()


class Music:
    volume = True
    def __init__(self):
        self.menu = self.Menu(self)
        self.game = self.Game(self)

    class Menu:
        def __init__(self, music):
            self.music = music
            self.sound = pygame.mixer.Sound("data/audio/menu.mp3")

        def play(self):
            if self.music.volume:
                pygame.mixer_music.load('data/audio/menu.mp3')
                pygame.mixer_music.play(-1)

        def stop(self):
            pygame.mixer_music.pause()

    class Game:
        def __init__(self, music):
            self.music = music
        def play(self):
            if self.music.volume:
                pygame.mixer_music.load('data/audio/game.mp3')
                pygame.mixer_music.play(-1)

        def stop(self):
            pygame.mixer_music.stop()






