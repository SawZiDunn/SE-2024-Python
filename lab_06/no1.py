def get_grade(mark):
    if 80 <= mark <= 100:
        return "A"
    elif 70 <= mark < 80:
        return "B"
    elif 60 <= mark < 70:
        return "C"
    elif 50 <= mark < 60:
        return "D"
    elif 0 <= mark < 50:
        return "F"
    else:
        print("Invalid mark!")
        return

print(f"You get {get_grade(55)}")