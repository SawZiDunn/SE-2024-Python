def main():
    x = int(input("Input an integer not less than 1: "))
    while x < 1:
        x = int(input("Input an integer not less than 1: "))

    for a in range(x, 0, -1):
        for i in range(a):
            print("*" * (i + 1), end="\n")
    
        temp = 0 if a == 2 else 1

        for k in range(a - 1 - temp):
            print("*" * (a - k - 1), end="\n")
      
        print("=====")

def main0():
    x = int(input("Input an integer not less than 1: "))
    while x < 1:
        x = int(input("Input an integer not less than 1: "))

    for a in range(x, 0, -1):
        if a == 1:
            print("*")

        for i in range( a):
            for _ in range( i + 1):
                print("*", end="")
            print()

        for k in range(a - 1, 1, -1):
            for _ in range(k):
                print("*", end="")
            print()
            
main0()