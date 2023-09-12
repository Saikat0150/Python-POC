"""
Flyweight Design Pattern - is structural design pattern
"""
from typing import *


class SmartPhone:
    """
    SmartPhone(Flyweight)
    """
    def __init__(self, properties: List):
        self._properties = properties

    def sell(self, owner: str, price: int):
        """
        Selling operation on smartphone(flyweight object)
        which takes unique values per smartphone
        """
        common = self._properties
        print(f"Smartphone {common} is sold to {owner} for price {price}")

    def __repr__(self) -> str:
        return f'SmartPhone(properties={self._properties})'


class SmartPhoneFactory:
    """
    Smartphone(Flyweight) factory
    """
    _smartphones: Dict[str, SmartPhone] = {}

    def get_smartphone(self, properties: List) -> SmartPhone:
        """
        Return SmartPhone(Flyweight) object
        This method creates new object and cache it if does not exist
        """
        key = '-'.join(properties)
        if key in self._smartphones:
            print(f"Returning already existing Smartphone object for {properties}")
        else:
            print(f"New Smartphone object created for {properties}")
            self._smartphones[key] = SmartPhone(properties)
        return self._smartphones[key]

    def list_smartphones(self) -> list[SmartPhone]:
        """
        List down all the Smartphones
        """
        smartphones = self._smartphones.values()
        for item in smartphones:
            print(item)


if __name__ == "__main__":
    fact = SmartPhoneFactory()
    smartphone = fact.get_smartphone(['Apple','iphone 14', 'Black', '128GB'])
    smartphone.sell('Hardik', 59000)

    smartphone = fact.get_smartphone(['Apple', 'iphone 13', 'Black', '128GB'])
    smartphone.sell('Aarav', 49000)

    smartphone = fact.get_smartphone(['Samsung', 'Galaxy S23', 'White', '128GB'])
    smartphone.sell('Shailaja', 63000)

    smartphone = fact.get_smartphone(['Apple', 'iphone 14', 'Black', '128GB'])
    smartphone.sell('Aarav', 59000)

    fact.list_smartphones()
