from prac_06.information import Information

def main():
    informations = []
    first_name = str(input("First name :"))
    while first_name != "" and first_name != " ":
        last_name = str(input("Last name :"))
        age = int(input("Age :"))
        information_add = Information(first_name, last_name, age)
        informations.append(information_add)
        first_name = str(input("First name :"))
    print("First name   Last name   Age")
    for information in informations:
        print(information)

main()
