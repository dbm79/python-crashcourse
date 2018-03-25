from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    ''' Return the Pygal 2-digit country code for the given country '''

    for code, name in COUNTRIES.items():
        # Go through the dictionary looking for the country name
        if name == country_name:
            return code
        else:
            return "Country Name Not Found!"
