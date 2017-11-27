import csv
import numpy as np

n = 9

def will_live (row):
    alive = row[0]
    neighbours = row[1:]
    num_of_neighbours = sum(neighbours)
    if num_of_neighbours < 2:
        return 0
    if num_of_neighbours == 2:
        return alive
    if num_of_neighbours == 3:
        return 1
    if num_of_neighbours > 3:
        return 0

def make_random_subset_of_cases (m):
    noise = np.random.choice([0, 1], size=(m, n), p=[2./3, 1./3])
    with open('random_subset_of_cases.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
        wr.writerow([m, n, 'dead', 'alive'])
        for row in noise:
            row = row.tolist()
            wr.writerow(row + [will_live(row)])

make_random_subset_of_cases(200)

def make_all_possible_cases ():
    with open('all_possible_cases.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_MINIMAL)
        wr.writerow([2**n, n, 'dead', 'alive'])
        for i in range(0, 2**n):
            row = map(int, list("{0:b}".format(i).zfill(n)))
            wr.writerow(row + [will_live(row)])

make_all_possible_cases()

