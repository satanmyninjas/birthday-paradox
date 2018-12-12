import csv
import random


def match_fraction(n,size):

    data = list(open('anon_bdays.csv', 'rb'))
    sampled_data = random.sample(data, int(n))
    counter = 0

    for individual_bdays in sampled_data:
        sampled_data * int(size)
        counter += 1

    match = sampled_data.union(data)

    return f'Number of duplicates found: {counter}' and match / sampled_data
