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

#-------------------------------------------------

# simple class example_Restaurant

class Restaurant():

    def __init__ (self, Restaurant_name, Cuisine_type):

        self.Restaurant_name = Restaurant_name
        self.Cuisine_type = Cuisine_type

    def describe_Restaurant(self):
       print (f"The Restaurant name is {self.Restaurant_name}")
       print (f"The cuisine type is {self.Cuisine_type}")

    def open_Restaurant(self):
       print(f"The Restaurant {self.Restaurant_name} is open")

Restaurant1 = Restaurant('supermacs', 'pizza')
Restaurant2 = Restaurant('burgerking', 'burger')

Restaurant1.describe_Restaurant()
Restaurant1.open_Restaurant()
Restaurant2.open_Restaurant()