cars = ['bmw', 'audi', 'toyota', 'subaru']

print(sorted(cars)) # This will sort the list but not modify it

cars.reverse()  # This will revers the order of the list in-place
print(cars)

cars.sort() # This will sort the list in-place (modify it)
print(cars)

cars.sort(reverse=True) #This will sort the list in reverse
print(cars)

print(len(cars))    # This will print the number (length) of the list
