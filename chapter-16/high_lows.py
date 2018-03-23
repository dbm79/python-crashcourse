import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)

    # Get the highs for the days
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
print(highs)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs)
plt.title('Daily high tempuratures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Tempurature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
