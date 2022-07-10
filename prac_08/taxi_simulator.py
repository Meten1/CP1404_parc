from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    menu = "q)uit, c)hoose taxi, d)rive"
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    current_bill = 0
    print("Let's drive!")
    print(menu)
    menu_choice = str(input(">>>")).upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available: ")
            for number in range(0, len(taxis)):
                print("{} - {}".format(number, taxis[number]))
            car_choice = int(input("Choose taxi: "))
            if car_choice > len(taxis) - 1:
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[car_choice]
        elif menu_choice == "D":
            if current_taxi == None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                driving_distance = int(input("Drive how far?"))
                current_taxi.drive(driving_distance)
                cost = current_taxi.get_fare()
                current_bill += cost
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, cost))
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(current_bill))
        print(menu)
        menu_choice = str(input(">>>")).upper()
    print("Total trip cost: {:.2f}".format(current_bill))
    print("Taxis are now:")
    for number in range(0, len(taxis)):
        print("{} - {}".format(number, taxis[number]))



main()
