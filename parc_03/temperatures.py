"""
CP1404/CP5632 - Practical
Temperature conversions
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            fahrenheit = float(input("Fahrenheit : "))
            celsius = calculate_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def calculate_fahrenheit(celsius):
    result = celsius * 9.0 / 5 + 32
    return result


def calculate_celsius(fahrenheit):
    result = 5 / 9 * (fahrenheit - 32)
    return result

main()