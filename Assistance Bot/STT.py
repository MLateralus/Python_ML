import speech_recognition as sr
from gtts import gTTS
import os
import time


class STT:
    def __init__(self, user_name):
        self.r = sr.Recognizer()
        self.user_name = user_name
        self.say_hello(user_name)

        with open('credentials/WIT.txt') as f:
            self.WIT_AI_KEY = f.readline()
            f.close()

        # Debug the config
        print("[DEBUG] Using WIT key: %s" % self.WIT_AI_KEY)
        print("[DEBUG] sr.energy_threshold: %s" % self.r.energy_threshold)

    def listen(self):
        with sr.Microphone() as source:
            print("Listening... ")
            audio = self.r.listen(source)
        return self.recognize_wit(audio)

    def recognize_wit(self, audio):
        print("Trying WIT ...")
        try:
            return self.r.recognize_wit(audio, key=self.WIT_AI_KEY)
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0}".format(e))

    # Redesign this to autoclose the audio file on windows !
    def say_hello(self, user_name):
        tts = gTTS('Cześć' + user_name, lang='pl')
        tts.save("hello.mp3")
        os.system("hello.mp3")
        time.sleep(2) # Ughh..

if __name__ == "__main__":

    # Create a new Instance for user
    stt_x = STT("Majeczka")

    # recog_text = stt_x.listen()
