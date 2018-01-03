import speech_recognition as sr


class x_STT:

    def __init__(self):
        self.r = sr.Recognizer()
        self.WIT_AI_KEY = ''
        with open('credentials/WIT.txt') as f:
            self.WIT_AI_KEY = f.readline()
            f.close()
        assert (self.WIT_AI_KEY != ''), "WIT KEY not available"

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