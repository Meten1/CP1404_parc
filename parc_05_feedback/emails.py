def main():
    EMAIL_TO_NAME = {}
    email = str(input("Email: "))
    while email != "":
        name = get_name(email)
        EMAIL_TO_NAME[email] = name.title()
        email = str(input("Email: "))
    print_information(EMAIL_TO_NAME)

def get_name(email):
    name_extract, email_symbol, domain_name = email.partition("@")
    first_name, point, last_name = name_extract.partition(".")
    choice = str(input(f"Is your name {first_name.capitalize()} {last_name.capitalize()} ? (Y/N)")).upper()
    if choice == "N" or choice == "NO":
        name = str(input("Name: "))
    else:
        name = first_name + " " + last_name
    return name

def print_information(EMAIL_TO_NAME):
    for key, value in EMAIL_TO_NAME.items():
        print(f"{value}({key})")


main()

