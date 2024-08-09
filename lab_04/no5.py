total = 0
for i in range(5):
    x = int(input("Enter an integer: "))
    if x < 0:
        if total >= 0:
            total = 0
        total += x
    else:
        if total < 0:
            total = 0
        total += x

    print("Current sum: " + str(total))