from prac_06.guitar import Guitar

def main():
    gibson = Guitar("Gibson", 1922)
    another_guitar = Guitar("another_guitar", 2013)
    guitars = [gibson, another_guitar]
    for guitar in guitars:
        print(guitar.get_age())
    for guitar in guitars:
        print(guitar.is_vintage())

main()
