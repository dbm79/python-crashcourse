class Car():
    '''A simple attempt to model a car'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        '''Return a neatly formated descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''Print the car's mileage.'''
        print('This car has ' + str(self.odometer) + ' miles on it.')

    def update_mileage(self, miles):
        '''Update the mileage attribute'''
        '''Reject if you try to roll mileage backwards'''
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print('You cannot roll the miles backwards')

my_new_car = Car('kia', 'sorento', 2017)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
my_new_car.update_mileage(15000)
print(my_new_car.read_odometer())

my_new_car.update_mileage(5000)
