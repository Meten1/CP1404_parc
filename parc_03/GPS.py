import random

def main():
    gophers_numbers = 1000
    start_year = 1
    final_years = 10
    welcome_words = "Welcome to the Gopher Population Simulator!\nStarting population: {}\nYear {}".format(gophers_numbers, start_year)
    print(welcome_words)
    for year in range(start_year + 1, final_years + 1):
        increase_numbers = get_increase_numbers(gophers_numbers)
        dwindle_numbers = get_dwindle_numbers(gophers_numbers)
        gophers_numbers += increase_numbers
        gophers_numbers -= dwindle_numbers
        print("{} gophers were born. {} died.".format(increase_numbers, dwindle_numbers))
        print("Population: {}".format(gophers_numbers))
        print("Year {}".format(year))

def get_increase_numbers(gophers_numbers):
        born_numbers = random.randint(10, 21) * 0.01 * gophers_numbers
        return int(born_numbers)


def get_dwindle_numbers(gophers_numbers):
        die_numbers = random.randint(5, 26) * 0.01 * gophers_numbers
        return int(die_numbers)

main()