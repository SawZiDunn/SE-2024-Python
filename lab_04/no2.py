x = eval(input("Enter somthing: "))

if type(x) == float:
    choice = int(input("floating point(1) or scientiic format(2)?: "))
    if choice == 1:
        print(f"{x:.2f}")
    elif choice == 2:
        print(f"{x:.2e}")
    else:
        
     print("Invalid Choice")

elif type(x) == int:
    choice = int(input("binary(1), octal(2), hexadecimal(3), decimal(4) format?: "))
    if choice == 1:
        print(bin(x))
    elif choice == 2:
        print(oct(x))
    elif choice == 3:
        print(hex(x))
    elif choice == 4:
        print(x)
    else:
        print("Invalid Choice")