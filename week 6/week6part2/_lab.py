class Car: 
    def __init__(self, color, model, year): 
        self.color= color 
        self.model=model 
        self.year= year 
    def drive(self):    
        print(F"The {self.color} {self.model} is driving.") 
    def stop(self): 
        print(f"The {self.color} {self.model} has stopped.") 
    def display_info(self): 
        print(f"Car Info: {self.year} {self.color} {self.model}") 
class ElectricCar(Car): 
    def __init__(self, color, model, year, battery_capacity): 
        super().__init__(color, model, year) 
        self.battery_capacity= battery_capacity 
        
    def display_info(self): 
        super().display_info() 
        print(f"Battery Capacity: {self.battery_capacity} kwh") 
    #Create an ElectricCar instance 
my_electric_Car = ElectricCar("white","Tesla Model 3", 2022, 75) 
my_electric_Car.drive()
my_electric_Car.stop()
my_electric_Car.display_info()


