import csv
from collections import namedtuple


def main():
    input_file = open('guitars.csv', 'r', newline='')
    guitar = namedtuple('Guitar', 'name, year, cost')
    reader = csv.reader(input_file)
    for row in reader:
        guitar = guitar._make(row)
        print(repr(guitar))


main()
