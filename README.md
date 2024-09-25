"""

Author:Badal Rana
Program: To show electiric car simulation

"""
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
#to display the car info
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

4. Single Responsibility Principle (SRP)
Principle Explanation: A class should have only one reason to change, meaning it should only have one job or responsibility.

Code Application:
In our Car and ElectricCar classes, each class is focused on a specific aspect of a car: Car deals with general car functionalities, while ElectricCar manages electric-specific attributes like battery capacity.
class Car: 
    # Responsibilities: Define general car properties and behaviors
If a requirement changes for electric cars, only the ElectricCar class needs modification, preserving the integrity of the Car class.

5. Liskov Substitution Principle (LSP)
Principle Explanation: Subtypes must be substitutable for their base types without affecting the correctness of the program. If a class is a subclass, it should be able to replace its superclass without any issues.
Code Application:
The ElectricCar class should behave like a Car. Any function that uses a Car type should work correctly with an ElectricCar instance.
Example:

python
Copy code
def test_car(car: Car):
    car.drive()
    car.stop()
    car.display_info()

my_electric_car = ElectricCar("white", "Tesla Model 3", 2022, 75)
test_car(my_electric_car)  # This should work without any issues.
This demonstrates that ElectricCar can be used wherever a Car is expected, thus satisfying LSP.

6. Interface Segregation Principle (ISP)
Principle Explanation: Clients should not be forced to depend on interfaces they do not use. This principle is about splitting larger interfaces into smaller, more specific ones.

Code Application:
While the current implementation does not explicitly utilize interfaces, we can imagine that if we were to add features for different types of vehicles (like flying cars), we could create specific interfaces for each vehicle type instead of forcing all classes to implement methods they don’t need.
Example:

python
Copy code
class Drivable:
    def drive(self):
        pass

class Stoppable:
    def stop(self):
        pass

class Car(Drivai, Stoppable):
    # Implementation
This way, a flying car class would not need to implement drive if it doesn’t make sense, adhering to ISP.

7. Dependency Inversion Principle (DIP)
Principle Explanation: High-level modules should not depend on low-level modules; both should depend on abstractions. Additionally, abstractions should not depend on details, details should depend on abstractions.
Code Application:
In our case, we could refactor the car behavior into interfaces or abstract classes. For example, if we had a CarEngine class, the Car class could depend on it rather than a concrete engine implementation.
Example:

python
Copy code
class Engine:
    def start(self):
        pass

class ElectricEngine(Engine):
    def start(self):
        print("Electric engine starting...")

class Car:
    def __init__(self, engine: Engine):  
        self.engine = engine

def drive(self):
        self.engine.start()
        print("Driving...")
This decouples the Car class from specific engine implementations, enhancing flexibility and testability.



