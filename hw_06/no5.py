def check_notes():
    amount = int(input("Input your amount of money: "))
    notes = [1000, 500, 100, 50, 20, 5, 2, 1]

    for i in notes:
        count = amount // i
        amount -= count * i
        if count != 0:
            if i in [2, 1]:
                print(f"{i}-Baht coins: {count}")

            else:
                print(f"{i}-Baht notes: {count}")

check_notes()