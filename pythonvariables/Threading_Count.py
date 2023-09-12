from threading import *
import time


def sleep(x):
    print("Thread %x going to sleep for 2 seconds." % x)
    time.sleep(2)
    print("Thread %x is active now. " % x)


for x in range(10):
    th = Thread(target=sleep, args=(x, ))
    th .start()
    print("Current Thread count: %x." % active_count())
