class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("Dog barking")


d = Dog()
d.bark()
d.speak()