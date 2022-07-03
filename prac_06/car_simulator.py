from prac_06.car import Car


def main():
    current_fuel = 100
    odo = 0
    menu = "Menu:\nd) drive\nr) refuel\nq) quit"
    print("Let's drive!")
    name = str(input("Enter your car name: "))
    name_car = Car(name, current_fuel)
    print("{}, fuel= {}, odo= {}".format(name, current_fuel, odo))
    print(menu)
    choice = str(input("Enter your choice:")).upper()
    while choice != "Q" and choice != "QUIT":
        if choice == "D" or choice == "DRIVE":
            moving_distance = int(input("How many km do you wish to drive?"))
            while moving_distance < 0:
                print(" Distance must be >= 0")
                moving_distance = int(input("How many km do you wish to drive?"))
            if moving_distance < current_fuel:
                name_car.drive(moving_distance)
                current_fuel = name_car.fuel
                odo = name_car.odometer
                print("The car drove {}km.".format(moving_distance))
            else:
                name_car.drive(moving_distance)
                residual_fuel = current_fuel
                current_fuel = name_car.fuel
                odo = name_car.odometer
                print("The car drove {}km and ran out of fuel.".format(residual_fuel))
        elif choice == "R" or choice == "REFUEL":
            fuel_add = int(input("How many units of fuel do you want to add to the car?"))
            while fuel_add < 0:
                print("Fuel amount must be >= 0")
                fuel_add = int(input("How many units of fuel do you want to add to the car?"))
            name_car.add_fuel(fuel_add)
            current_fuel = name_car.fuel
            print("Added {} units of fuel.".format(fuel_add))


        else:
            print("Please enter the correct option")
        print("{}, fuel= {}, odo= {}".format(name, current_fuel, odo))
        print(menu)
        choice = str(input("Enter your choice:")).upper()
    print("Good bye {}'s driver.".format(name))
    exit()



main()
