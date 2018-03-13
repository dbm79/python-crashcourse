def describe_pets(pet_name, animal_type='dog'):
    '''Display information about a pet.'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() )

describe_pets('dog', 'hulk')

#Example of passing keyword arguments
describe_pets(animal_type='dog', pet_name='daisy')

#example of calling function with default value
describe_pets(pet_name='tank')
