class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe(self):
        print(f"{self.year} {self.make} {self.model}")
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Tesla", "Model 3", 2023)

cars = [car1, car2, car3]

for c in cars:
    c.describe()

