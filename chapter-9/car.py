class Car():
    '''A simple attempt to model a car'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''Return a neatly formated descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('kia', 'sorento', 2017)
print(my_new_car.get_descriptive_name()) 
