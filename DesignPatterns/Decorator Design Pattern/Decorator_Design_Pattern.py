import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class Abstrat_Coffee(object):
    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.16*self.get_cost()


class Concrete_Coffee(Abstrat_Coffee):
    def get_cost(self):
        return 10.00

    def get_ingredients(self):
        return "Coffee"


@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstrat_Coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


class Sugar(Abstract_Coffee_Decorator):
    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() +", Sugar"


class Milk(Abstract_Coffee_Decorator):
    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 4

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() +", Milk"


class Vanilla(Abstract_Coffee_Decorator):
    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 8

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() +", Vanilla"

