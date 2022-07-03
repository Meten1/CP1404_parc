from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    guitar_name = str(input("Name: "))
    while guitar_name != "" and guitar_name != " ":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_add)
        print(guitar_add)
        guitar_name = str(input("Name: "))
    # guitars.append((Guitar("Fender Stratocaster", 2014, 765.40)))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)


main()