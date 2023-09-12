from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30 Kmpl")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25 Kmpl")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24 Kmpl")


class Honda(Car):
    def mileage(self):
        print("The mileage is 27 Kmpl")


t = Tesla()
t.mileage()

h = Honda()
h.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()