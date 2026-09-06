"""A set of classes used to represent gas and electric cars."""

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year, fuel):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name.title())

    def refill(self):
        print(f'This car should be filled with {self.fuel}')

    def test_drive(self):
        """Print a statement showing the car is driving."""
        print("You are driving your " + self.model.title() + " how does it handle?")

car1 = Car('audi', 'A6', 2013, 'diesel')
car2 = Car('Smart', 'ForTwo', 2010, 'petrol')
car3 = Car('Ford', 'Mustang', 2020, 'petrol')
car4 = Car('BYD', 'Seal', 2023, 'electric')

car1.get_descriptive_name()
car2.test_drive()
car3.refill()
car4.refill()
car1.test_drive()