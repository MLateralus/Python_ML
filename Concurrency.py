from threading import Thread
from time import sleep

class One(Thread):

    def __init__(self):
        Thread.__init__(self)
        print("Constructor")

    def run(self):
        print("Thread started...")
        x = 0
        while (x < 10):
            print("Loop of while %d:" % x)
            sleep(2)
            x += 1
        print("Thread ended")

print("Main process started")

once = One()
once.start()
print("Main process ended")