from threading import *

# Declaring a lock
lock = Lock()
deposit = 50


def add_profit():
    global deposit
    print(deposit)
    for i in range(100):
        lock.acquire()
        deposit += 10
        lock.release()
        print(deposit)
    print("Final: ", deposit)


def pay_bill():
    global deposit
    print(deposit)
    for i in range(100):
        lock.acquire()
        deposit -= 10
        lock.release()
        print(deposit)


# Creating threads
thread1 = Thread(target=add_profit, args=())
thread2 = Thread(target=pay_bill, args=())
# Starting the threads
thread1.start()
thread2.start()
# Waiting for both the threads to finish executing
thread1.join()
thread2.join()
print(deposit)
