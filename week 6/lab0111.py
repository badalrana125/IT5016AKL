class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.Year = year 

    def car(self):
        print(f"Color: {self.color},Model {self.model}, Year : {self.Year}")

car1 = Car("black", "tesla model s",2024)
car1.car()
