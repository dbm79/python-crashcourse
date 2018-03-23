import csv

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    print(header_row)
