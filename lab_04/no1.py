while True:
    x = int(input("Input your score: "))
    if 0 <= x <= 100:
        break
    else:
        print("Must be from 0 to 100!")
        continue

if 80 <= x <= 100:
    print("Grade A")
elif 70 <= x < 80:
    print("Grade B")
elif 60 <= x < 70:
    print("Grade C")
elif 50 <= x < 60:
    print("Grade D")
elif 0 <= x < 50:
    print("Grade F")

