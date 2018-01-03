import tts
import stt
import pywapi


class Brain:
    def __init__(self):
        self.tts = tts.x_TTS('pl')
        self.stt = stt.x_STT()

    def say_hello(self, user_name):
        self.tts.greet(user_name)

    def listen(self):
        self.stt.listen()


class Actions:
    def __init__(self):
        pass

    def weather(self):
        # Tatra Mountain: {'LOXX0072': 'Strbske Pleso, PV, Slovakia'}
        weather_com_result = pywapi.get_weather_from_weather_com('LOXX0072')
        print("weather_com_result: %s " % weather_com_result)
        print("Weather.com says: It is " + (weather_com_result['current_conditions']['text']) + " and " +
            weather_com_result['current_conditions']['temperature'] + "C Strbske Pleso, Slovakia.\n\n")


if __name__ == "__main__":

    # Create a new Instance for user
    instance = Brain()
    # instance.say_hello("Majkel")
    # instance.listen()

    x_ahs_action = Actions()
    x_ahs_action.weather()
