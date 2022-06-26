
manu = "i\nii\niii\niv"
min_number = int(input("Enter min_number: "))
max_number = int(input("Enter max_number: "))

print(manu)
choice = str(input("Please choose: "))
while choice != "iv":
    if choice == "i":
        for i in range(min_number, max_number + 1):
            if i % 2 == 0:
                print(i, end=" ")
    elif choice == "ii":
        for i in range(min_number, max_number + 1):
            if i % 2 == 1:
                print(i, end=" ")
    elif choice == "iii":
        for i in range(1, max_number + 1):
            for j in range(1, min_number + 1):
                print("*", end="")
            print()
    print()
    choice = str(input("Please choose: "))
print("Finished.")