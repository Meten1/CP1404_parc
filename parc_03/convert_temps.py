

def main():
    INPUT_FILE = "temps_input.txt"
    OUTPUT_FILE = "temps_output.txt"
    input_file = open(INPUT_FILE, "r")
    output_file = open(OUTPUT_FILE, "a")
    fahrenheit_list = input_file.readlines()
    for fahrenheit in fahrenheit_list:
        celsius = calculate_celsius(float(fahrenheit))
        print("{}".format(celsius), file = output_file)
    input_file.close
    output_file.close


def calculate_celsius(fahrenheit):
    result = 5 / 9 * (fahrenheit - 32)
    return result

main()