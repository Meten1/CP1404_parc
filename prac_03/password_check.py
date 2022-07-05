def main():
    min_length = 6
    password = get_password(min_length)
    the_password(password)

def get_password(min_length):
    input_password = str(input("Enter your password: "))
    while len(input_password) < min_length:
        print("Please enter a password of at least {} digits!".format(min_length))
        input_password = str(input("Enter your password: "))
    return input_password

def the_password(password):
    for char in password:
        print("*", end="")

main()






