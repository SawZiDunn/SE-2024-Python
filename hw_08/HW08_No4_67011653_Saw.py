def find_10th_digit():
    x = input("Enter the first 9 digits of an ISBN-10 as a string: ")
    total = 0
    for i in range(len(x)):
        total += int(x[i]) * (i + 1)
    tenth_digit = total % 11

    x += 'X' if tenth_digit == 10 else str(tenth_digit)
    print(f"Your ISBN-10 number is {x}.")

find_10th_digit()