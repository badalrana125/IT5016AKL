class Person():
    # constructor 
    def __init__(self, name, gender):
        self.name = name
        self.age = 10
        self.gender = gender

    def speaks(self):
            quote = input(f"what does the {self.name} say?: ")
            quote = input(f"The age is {self.age}")
            quote = input(f"The gender is {self.gender}")
            print(quote)

#object
person1 = Person("badal", "male")
person2 = Person("kanchan", "Female")

person1.speaks()