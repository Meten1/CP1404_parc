
#1

OUT_FILE = "name.txt"
out_file = open(OUT_FILE, 'w')

name = str(input("Please enter your name: "))
print(name, file=out_file)

out_file.close()



#2

OUT_FILE = "name.txt"
out_file = open(OUT_FILE, "r")
print(f"You name is {out_file.read()}")

out_file.close()



#3

OUT_FILE = 'numbers.txt'
out_file = open(OUT_FILE, "r")
numbers_list = out_file.readlines()
print(int(numbers_list[0]) + int(numbers_list[1]))
out_file.close()


#4

OUT_FILE = 'numbers.txt'
out_file = open(OUT_FILE, "r")
numbers_list = out_file.readlines()
total_numbers = 0
for i in range(len(numbers_list)):
    total_numbers += int(numbers_list[i])
print(total_numbers)

out_file.close()

