
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a.

for i in range(0, 101, 10):
    print(i, end=" ")
print()

#b.

for i in range(20, 0, -1):
    print(i, end=" ")
print()



#c.

stars_number = int(input("Number of stars: "))
for i in range(0, stars_number): #Because the range is (x, y], for simplicity of writing, (1, n+1) is changed to (0, n)
    print("*", end="")
print()



# d.

stars_number = int(input("Number of stars: "))
incremental_number = 1
for i in range(0, stars_number):
    for j in range(0, incremental_number):
        print("*", end="")
    incremental_number = incremental_number + 1
    print()
