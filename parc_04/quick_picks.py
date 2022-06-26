import random


def main():
    pick_number = int(input("How many quick picks? "))
    for pick in range(1, pick_number + 1):
        numbers = []
        while len(numbers) < 6:
            number = random.randint(1,46)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        for element in numbers:
            print("{:2}".format(element), end=" ")
        print()


main()