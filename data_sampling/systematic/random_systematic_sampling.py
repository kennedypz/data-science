population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

populationSize = len(population)

systematicSample = []

# gets one item from the list, skips two, gets the third and repeat
# until the list is over
for i in range(0, populationSize, 3):
    systematicSample.append(population[i])

print(systematicSample)
