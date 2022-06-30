string_list = []
STRING_TO_FREQUENCY = {}
input_string = str(input("Enter the string: "))
while input_string != "":
    string_list.append(input_string)
    STRING_TO_FREQUENCY[input_string] = string_list.count(input_string)
    input_string = str(input("Enter the string: "))
for key, value in STRING_TO_FREQUENCY.items():
    print(f"{key:{len(max(string_list))}} : {value}")

