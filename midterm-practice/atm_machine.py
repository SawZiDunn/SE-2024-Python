def withdraw():
    amount = 0
    while True:
        amount = int(input("How much you want to withdraw: "))
        if amount % 100 == 0:
            break
    
    thousand_notes = 0
    five_hundred_notes = 0
    hundred_notes = 0

    thousand_notes = amount // 1000
    amount -= 1000 * thousand_notes

    five_hundred_notes = amount // 500
    amount -= 500 * five_hundred_notes

    hundred_notes = amount // 100

    print(f"You get: {thousand_notes} notes of 1,000 Bahts\n{five_hundred_notes} notes of 500 Bahts\n{hundred_notes} notes of 100 Bahts")



withdraw()