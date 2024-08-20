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
      
        # print("=====")
            
main()