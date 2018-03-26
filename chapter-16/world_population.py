import json
import country_codes
from pygal.maps.world import World

# Load the data into a list
filename = 'population_data.json'

with open(filename) as f_obj:
    pop_data = json.load(f_obj)

# build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        code = country_codes.get_country_code(country_name)

        if code:
            cc_populations[code] = population

wm = World()
wm.title = 'World Population in 2010, by Country '
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')
