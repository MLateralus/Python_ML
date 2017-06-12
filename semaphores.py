import threading
import time
import random

semafor = threading.Semaphore(0)

def producer(sleep_amount):
    print("Producer started.. for amount %d" % sleep_amount)
    print("Producer semafor...")
    time.sleep(sleep_amount)
    semafor.release()

def consumer(sleep_amount):
    print("Customer started.. for amount %d" % sleep_amount)
    semafor.acquire()
    print("Consumer semafor...")


if __name__ == '__main__':
    thr1 = threading.Thread(target = producer, args = (random.randint(0,5),))
    thr2 = threading.Thread(target = consumer, args = (random.randint(0,5),))
    thr1.start()
    thr2.start()
    print("Started...")