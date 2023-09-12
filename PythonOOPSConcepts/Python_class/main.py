class car:
    def __init__(self, modelName, year):
        self.modelName = modelName
        self.year = year

    def display(self):
        print(self.modelName, self.year)


c1 = car("Toyota", 2016)
c1.display()