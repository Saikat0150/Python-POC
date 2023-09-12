"""
Pattern name - Singleton (Mono state pattern)
Pattern Type - Creational Design Pattern
"""


# Solution - 2
class Borg(object):
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared


class SingleTon(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg


o1 = SingleTon("Saikat")
print("Object - 1 ==>", o1)
print("Object - 1 val ==>", o1.val)

o2 = SingleTon("Nilu")
print("Object - 2 ==>", o2)
print("Object - 2 val ==>", o2.val)
print("Object - 1 val ==>", o1.val)
