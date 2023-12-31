"""
Provide an interface to create the related or dependent
objects without specifying the classes
"""

from abc import ABCMeta, abstractmethod


class CarFactory(metaclass=ABCMeta):
    @abstractmethod
    def build_parts(self):
        pass

    @abstractmethod
    def build_car(self):
        pass


class SedanCarFactory(CarFactory):
    def build_parts(self):
        return SedanCarPartsFactory()

    def build_car(self):
        return SedanCarAssesbleFactory()


class SuvCarFactory(CarFactory):
    def build_parts(self):
        return SuvCarPartsFactory()

    def build_car(self):
        return SuvCarAssesbleFactory()


class CarPartsFactory(metaclass=ABCMeta):
    """
    Declare an interface for a type of car parts
    """
    @abstractmethod
    def build(self):
        pass


class SedanCarPartsFactory(CarPartsFactory):
    def build(self):
        print("Sedan car parts are built")

    def __str__(self):
        return '<Sedan car parts>'


class SuvCarPartsFactory(CarPartsFactory):
    def build(self):
        print("SUV Car parts are built")

    def __str__(self):
        return '<SUV car parts>'


class CarAssembleFactory(metaclass=ABCMeta):
    """
    Declare an interface for a type of cars.
    """
    @abstractmethod
    def assemble(self):
        pass


class SedanCarAssesbleFactory(CarAssembleFactory):
    def assemble(self, parts):
        print(f"Sedan car is assembled here using {parts}")


class SuvCarAssesbleFactory(CarAssembleFactory):

    def assemble(self, parts):
        print(f"SUV car is assembled here using {parts}")


if __name__ == '__main__':
    for factory in (SedanCarFactory(), SuvCarFactory()):
        car_parts = factory.build_parts()
        car_parts.build()
        car_builder = factory.build_car()
        car_builder.assemble(car_parts)
