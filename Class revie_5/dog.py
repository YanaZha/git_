from Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)

    def is_barking(self):
        print(f'{self.name}')