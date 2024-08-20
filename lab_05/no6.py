n = int(input("Enter the number of lines: "))

for i in range(n):

    if i < n // 2:
        for j in range(i, -1, -1):
            print(pow(2, j), end=" ")
    else:
        for j in range(n - i - 1, -1, -1):
            print(pow(2, j), end=" ")
    
    print()