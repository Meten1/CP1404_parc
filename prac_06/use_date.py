from prac_06.date import Date

def main():
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    data = Date(day, month, year)
    print(data)
    choice = str(input("Would you like to add days?(Y/N)")).upper()
    while choice == "Y" or choice == "YES":
        amount = int(input("Please enter the number of days to add: "))
        data.add_days(amount)
        print(data)
        choice = str(input("Would you like to add days?(Y/N)")).upper()
    print("Thank you for you use!")

main()