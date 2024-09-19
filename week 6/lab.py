# define a person class:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("james", 30)
person1.greet()

# define a rectangle class with methods for area and peremeter
class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectangle(4, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
