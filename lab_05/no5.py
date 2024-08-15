while True:
    c = input("Input a char: ")
    if c.isspace():
        print("Good bye, see you tomorrow")
        break
    elif len(c) != 1:
        print("Must be a char!")
        continue
    else:
        dec = ord(c)
        if 0x61 <= dec <= 0x7A:
            print(f"{c} is a small-case letter and it's capital letter is {c.upper()}")
        elif 0x41 <= dec <= 0x5A:
            print(f"{c} is a capital letter and it's small-case letter is {c.lower()}")
        elif 0x30 <= dec <= 0x39:
            print(f"{c} is a numeric character.")
        else:
            print(f"{c} is a special character.")






