import threading
from time import sleep

def funct(var, sleep_amount):
    print("Thread started nr: %d" % var)
    sleep(sleep_amount)
    print("var: " + str(var))
    print("Thread eneded.")


thr = threading.Thread(target = funct, args=(1,5))
thr2 = threading.Thread(target = funct, args=(2, 7))
thr3 = threading.Thread(target = funct, args=(3, 2))
thr.start()
thr2.start()
thr3.start()
