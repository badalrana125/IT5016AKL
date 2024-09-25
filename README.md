
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



*explaination of Software Design Principles:

1. DRY (Don't Repeat Yourself)
Principle: The DRY principle advocates for reducing code duplication. Each piece of knowledge should have a single, unambiguous representation in the system.
In the provided code, the display_info method in the ElectricCar class calls the display_info method of the parent Car class using super(). This avoids code duplication,
as the common functionality for displaying car information is centralized in the Car class.

Importance: By applying to the DRY principle, the code becomes easier to maintain and less error-prone. Changes to the way car information is displayed only need to be made in one place.

 def drive(self):    
        print(f"The {self.color} {self.model} is driving.") 

def stop(self): 
        print(f"The {self.color} {self.model} has stopped.") 

def display_info(self): 
        print(f"Car Info: {self.year} {self.color} {self.model}") 

2. KISS (Keep It Simple, Stupid)
Principle: The KISS principle emphasizes that systems should be kept as simple as possible. Complex designs can lead to confusion and increased likelihood of bugs.

Application: The implementation of the Car and ElectricCar classes is straightforward. Each method performs a clear and defined action (driving, stopping, displaying information).

Importance: Simple designs facilitate understanding for both current developers and future maintainers. If additional features are required later, the simplicity of the existing structure makes it easier to extend.
def drive(self):    
    print(f"The {self.color} {self.model} is driving.") 

3. Open/Closed Principle
Principle: The Open/Closed Principle states that classes should be open for extension but closed for modification. This means that the behavior of a class can be extended without changing its source code.
The ElectricCar class extends the Car class without altering the original Car class. This allows for adding electric-specific features (like battery_capacity) without modifying the existing Car class.

Importance: This principle promotes code reusability and flexibility. New types of cars can be created with different features without the risk of introducing bugs into existing code.

Code Application:
New car types can be created by extending the Car class without altering its code. For example, you could easily create a HybridCar class that inherits from Car.
   Code Example: The Car class can be extended with new vehicle types without modification.
   
class HybridCar(Car):
def __init__(self, color, model, year, battery_capacity, fuel_type):
        super().__init__(color, model, year)
        self.battery_capacity = battery_capacity
        self.fuel_type = fuel_type

def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")    

4. YAGNI (You Aren’t Gonna Need It)
The YAGNI principle suggests that you should not implement features until they are necessary. This prevents over-engineering and keeps the codebase clean.
Code Application:
The current implementation focuses on essential features: driving, stopping, and displaying information. No unnecessary methods or attributes are added.
Example: If you think you might need a charging method in the future, you can wait until it becomes necessary. For now, the classes remain simple.

5. Clean Code
Principle Explanation: Clean code is easy to read, understand, and maintain. It includes meaningful names, structured formatting, and minimal comments (if self-explanatory).
The naming conventions used (like drive, stop, display_info) clearly convey their purpose. The structure is clean, with consistent spacing and indentation.
def stop(self): 
    print(f"The {self.color} {self.model} has stopped.")



