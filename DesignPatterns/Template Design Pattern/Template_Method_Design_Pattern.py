"""
Template method Design Pattern - This is behavioural design pattern.
"""
from abc import *


class ThreeDaysTrip(metaclass=ABCMeta):
    @abstractmethod
    def transport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def back_to_home(self):
        pass

    def start(self):
        print("Trip is started")
        self.transport()
        self.day1()
        self.day2()
        self.day3()
        self.back_to_home()
        print("Trip is over")


class SouthTrip(ThreeDaysTrip):
    def transport(self):
        print("Go by train! Check in to the Hotel")

    def day1(self):
        print("Day-1: Enjoy the hotel beach whole day")

    def day2(self):
        print("Day-2: Visit historical places and Enjoy cruise life at night")

    def day3(self):
        print("Day-3: Enjoy shopping day with family and go anywhere you wish")

    def back_to_home(self):
        print("Check out and go Home by air!")


class NorthTrip(ThreeDaysTrip):
    def transport(self):
        print("Go by air! check in to hotel")

    def day1(self):
        print("Day-1: Go to very highted place and enjoy snow activities")

    def day2(self):
        print("Day-2: Enjoy river rafting and lavish dinner at night")

    def day3(self):
        print("Day-3: Enjoy shopping day with family and go anywhere you wish")

    def back_to_home(self):
        print("Check out and go Home by air!")


if __name__ == "__main__":
    place = input("Where do you want to go? North/South\n")
    if place.lower() == "north":
        trip = NorthTrip()
        trip.start()
    elif place.lower() == "south":
        trip = SouthTrip()
        trip.start()
    else:
        print(f"Sorry, we do not have any trip plan towards the {place.capitalize()}")