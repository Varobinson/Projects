class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)


car = Vehicle('Tesla', 'CyberTruck', 2022)
# print(car.make, car.model, car.year)
car.print_info()
