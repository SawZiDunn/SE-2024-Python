def phone_book():
    phone_numbers = dict()
    while True:
        print("\nPhonebook Manager")
        print("Press '+' to add a new contact.")
        print("Press '-' to delete a contact.")
        print("Press 'f' to find a contact.")
        print("Press 'p' to print out all contacts in the phone book.")
        print("Press 'q'")

        x = input("Enter your input: ")
        if x == "+":
            print()
            name = input("Name: ")
            ph_num = input("Phone Number: ")
            phone_numbers.update({name: ph_num})
        elif x == "-":
            name = input("Enter name to delete: ")
            phone_numbers.pop(name)
        elif x == "f":
            name = input("Enter name to find: ") 
            print(f"The phone number of {name} is {phone_numbers.get(name)}")
        elif x == "p":
            for (key, value) in phone_numbers.items():
                print(f"Name: {key}, Phone: {value}")
        elif x == "q":
            break
        else:
            continue

phone_book()