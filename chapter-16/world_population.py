import json

# Load the data into a list
filename = 'population_data.json'

with open(filename) as f_obj:
    pop_data = json.load(f_obj)

# Load 2010 population pop_data
for pop_dict in pop_data:
    print(pop_dict)
