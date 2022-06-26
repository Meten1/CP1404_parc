


def main():
    min_length = 6
    chars = str(input("Enter your password: "))
    while len(chars) < min_length:
        print("Please enter a password of at least {} digits!".format(min_length))
        chars = str(input("Enter your password: "))
    the_password(chars)

def the_password(chars):
    for i in chars:
        print("*", end="")

main()






