import pygame


class Main:
    MUSIC_PLAYED = False


class Menu:
    def __init__(self):
        self.sound = pygame.mixer.Sound("data/audio/menu.mp3")

    def play(self):
        pygame.mixer_music.load('data/audio/menu.mp3')
        pygame.mixer_music.play(-1)

    def stop(self):
        pygame.mixer_music.pause()


class Game:
    def play(self):
        pygame.mixer_music.load('data/audio/game.mp3')
        pygame.mixer_music.play(-1)

    def stop(self):
        pygame.mixer_music.stop()


class Clicked:
    def __init__(self):
        self.sound = pygame.mixer.Sound("data/audio/clicked.wav")

    def play(self):
        self.sound.play()


class Slap:
    def __init__(self):
        self.sound = pygame.mixer.Sound("data/audio/slap.mp3")

    def play(self):
        self.sound.play()


class Woosh1:
    def __init__(self):
        self.sound = pygame.mixer.Sound("data/audio/woosh1.wav")

    def play(self):
        self.sound.play()


class Woosh2:
    def __init__(self):
        self.sound = pygame.mixer.Sound("data/audio/woosh2.wav")

    def play(self):
        self.sound.play()


class Bell:
    def __init__(self):
        self.sound = pygame.mixer.Sound("data/audio/bell.mp3")

    def play(self):
        self.sound.play()
