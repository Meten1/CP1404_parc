
def main():
    print_permission = get_print_permission()
    if print_permission == False:
        print("Access denied")
        exit()
    else:
        print("Access granted")
        numbers = []
        for i in range(0,5):
            number = int(input("Number: "))
            numbers.append(number)
        print("The first number is {}".format(numbers[0]))
        print("The last number is {}".format(numbers[-1]))
        print("The smallest number is {}".format(min(numbers)))
        print("The largest number is {}".format(max(numbers)))
        print("The average number is {}".format(sum(numbers) / 5))

def get_print_permission():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                    'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                    'bob']
    username = str(input("Please enter your name: "))
    return username in usernames

# main()




def main2():
    print_permission = get_print_permission()
    if print_permission == False:
        print("Access denied")
        exit()
    else:
        print("Access granted")
        numbers = []

        number = int(input("Number: "))
        while number >= 0:
            numbers.append(number)
            number = int(input("Number: "))
        for i in range(1, len(numbers) + 1):
            print("Number {}: {}".format(i, numbers[i - 1]))


def get_print_permission():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = str(input("Please enter your name: "))
    return username in usernames

main2()