from threading import *
import time


def print_1():
    print("Starting of Thread : ",current_thread().name)
    time.sleep(2)
    print("Finishing of Thread : ", current_thread().name)


def print_2():
    print("Starting of Thread : ", current_thread().name)
    print("Finishing of Thread : ", current_thread().name)


a = Thread(target=print_1, name='Thread-1')
b = Thread(target=print_2, name='Thread-2', daemon=True)

a.start()
b.start()
