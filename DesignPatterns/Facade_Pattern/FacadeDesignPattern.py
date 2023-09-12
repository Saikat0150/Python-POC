"""
Facade Design Pattern
"""
class Cook(object):
    """
    Facade Class
    Desc: Provides easy interface for the client by calling all the
    classes that are seems difficult to use for the client
    """
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()

        self.boiler = Boiler()
        self.boiler.boilVegetable()

        self.frier = Frier()
        self.frier.fry()


class Cutter(object):
    """
    System class
    Desc: Cutter class provide feature of cutting vegetables
    """
    def cutVegetables(self):
        print("All vegetables are cut")


class Boiler(object):
    def boilVegetable(self):
        print("All vegetables are boiled")


class Frier(object):
    def fry(self):
        print("All vegetables are mixed and fried")


if __name__ == '__main__':
    # Using facade class to prepare dish
    cook = Cook()
    cook.prepareDish()