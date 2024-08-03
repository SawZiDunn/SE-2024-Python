def main():
    x = str(input("Enter a four-digit integer: "))
    # invalid input handling
    if len(x) != 4 or not x.isdigit():
        print("Must be 4-digit integer!")
    else:
        y = ""
        for i in range(1, len(x) + 1):
            y += x[-i]
        print(y)

        # there's also a shorter way
        # print(x[::-1])
    
    

main()