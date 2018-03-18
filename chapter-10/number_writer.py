import json

numbers = [2, 4, 6, 8, 10, 13, 15, 17]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
