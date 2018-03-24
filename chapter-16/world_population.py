import json
import country_codes

# Load the data into a list
filename = 'population_data.json'

with open(filename) as f_obj:
    pop_data = json.load(f_obj)

# Load 2010 population pop_data
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        print(country_name + ': ' + str(population))
