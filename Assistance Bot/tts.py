import pygame
from gtts import gTTS

class x_TTS:

    def __init__(self, lang):
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.lang_code = lang
        self.CLOCK_INTERVAL = 100

    def play_audio(self, file):

        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            self.clock.tick(self.CLOCK_INTERVAL)

        print("Audio finished")

    def greet(self, user_name):
        tts = gTTS('Cześć' + user_name, lang=self.lang_code)
        tts.save("greet.mp3")
        self.play_audio("greet.mp3")

    def speak(self, phase):
        tts = gTTS(phase, lang=self.lang_code)
        tts.save("response.mp3")
        self.play_audio("response.mp3")