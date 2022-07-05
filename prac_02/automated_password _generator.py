import random

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = get_random_password(MIN_LENGTH, MAX_LENGTH, SPECIAL_CHARACTERS)
    while not is_valid_password(password):
        print("Invalid password!")
        password = get_random_password(MIN_LENGTH, MAX_LENGTH, SPECIAL_CHARACTERS)
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED == True:
        if count_special == 0:
            return False

    # if we get here (without returning False), then the password must be valid
    return True


def get_random_password(MIN_LENGTH, MAX_LENGTH, SPECIAL_CHARACTERS):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    choice_list = "luds"
    random_password = ""
    minimum_lower_number = 1
    minimum_upper_number = 1
    minimum_digit_number = 1
    minimum_special_number = 1
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    password_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    for i in range(1, password_length + 1):
        if count_lower < minimum_lower_number:
            count = str(random.choice(alphabet)).lower()
            random_password += count
            count_lower += 1
        elif count_upper < minimum_upper_number:
            count = str(random.choice(alphabet)).upper()
            random_password += count
            count_upper += 1
        elif count_digit < minimum_digit_number:
            count = str(random.randint(0, 9))
            random_password += count
            count_digit += 1
        elif count_special < minimum_special_number:
            count = str(random.choice(SPECIAL_CHARACTERS))
            random_password += count
            count_special += 1
        else:
            one_choice = random.choice(choice_list)
            if one_choice == "l":
                count = str(random.choice(alphabet)).lower()
                random_password += count
            elif one_choice == "u":
                count = str(random.choice(alphabet)).upper()
                random_password += count
            elif one_choice == "d":
                count = str(random.randint(0, 9))
                random_password += count
            elif one_choice == "s":
                count = str(random.choice(SPECIAL_CHARACTERS))
                random_password += count
    password_list = list(random_password)
    random.shuffle(password_list)
    password = "".join(password_list)
    return password




main()