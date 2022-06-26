

numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0] = "ten"
numbers[-1] = 1
numbers_section = numbers[1:-1]
print(numbers, numbers_section)

if str(numbers[-2]).isdigit() == False:
    print("9 is not int")
else:
    print("9 is int")

