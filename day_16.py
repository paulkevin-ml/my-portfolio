class Car:
    total_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        Car.total_cars +=1
    
    def describe(self):
        print(f"{self.year} {self.make} {self.model} - {self.mileage} km")

    def drive(self, km):
        self.mileage += km
car1 = Car("Toyota", "Corolla", 2020)
car1.describe()
car1.drive(150)
car1.describe()
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Tesla", "Model 3", 2023)

print("Total cars created: ", Car.total_cars)
cars = [car1, car2, car3]

for c in cars:
    c.describe()

