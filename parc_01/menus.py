Guidoname = str(input("Enter name:"))
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = str(input(""))
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = str(input(""))
print("Finished.")
