
'''
max_number = 127
min_number = 33

character = str(input("Enter a character: "))
print("The ASCII code for {} is {}".format(character, ord(character)))

enter_number = int(input("Enter a number between 33 and 127: "))
while enter_number < min_number or enter_number > max_number:
    print("Please enter a value between 33-127!")
    enter_number = int(input("Enter a number between 33 and 127: "))
print("The character for {} is {}".format(enter_number, chr(enter_number)))
'''


def main():
    max_number = 127
    min_number = 33
    numbers = get_number(min_number, max_number)

    print("{:>3} {:>3}".format(numbers, chr(numbers)))



def get_number(min_number, max_number):
    numbers = str(input("Enter a number ({}-{}):".format(min_number, max_number)))
    while numbers.isdigit() == False or int(numbers) < min_number or int(numbers) > max_number:
        print("Please enter a valid number!")
        numbers = str(input("Enter a number ({}-{}):".format(min_number, max_number)))
    return int(numbers)

main()
