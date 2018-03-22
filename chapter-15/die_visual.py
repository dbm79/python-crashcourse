from die import Die

# Create a D6 Die
die = Die()

#Make some rolls and store them in a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
