from random import sample

population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

sample1 = sample(population, 4)
sample2 = sample(population, 4)
sample3 = sample(population, 4)
sample4 = sample(population, 4)

for i in range(4):
    print(sample(population, 4))


