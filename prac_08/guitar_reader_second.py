from prac_08.guitar import Guitar

def main():
    guitars = []
    input_file = open('guitars.csv', 'r')
    for line in input_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]) )
        guitars.append(guitar)

    for guitar in guitars:
        print(guitar)

    print(guitars)
    guitars.sort()
    print(guitars)

main()