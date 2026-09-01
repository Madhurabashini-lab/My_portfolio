class dog():
    #an attempt to model a cat
    def __init__(self, name, age):
        #assign the cats name and age
        self.name = name
        self.age = age

    def sleep(self):
        #The cat can sleep
        print(f"{self.name} is fast asleep like a little angel")

    def climb(self):
        #The cat can sleep
        print(f"Quick! {self.name} is climbing on the roof!")

my_dog = dog('noche', 4)

my_dog.sleep()
my_dog.climb()
#-------------------------------------------------

class student():
    def __init__(self, name, age, mark):
       self.name = name
       self.age = age
       self.mark = mark

    def display(self):
        print(f"{self.name} is from Cork")

    def number(self):
        print(f"{self.name} age is {self.age}")

    def numeric(self):
        print(f"{self.name} mark is {self.mark}")

my_student = student('Madhura', 30, 80)
my_student.display()
my_student.number()
my_student.numeric()