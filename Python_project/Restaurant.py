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




    