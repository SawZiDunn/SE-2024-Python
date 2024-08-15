def a():
    for i in range(5):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()

def b():
    for i in range(5):
        for j in range( 5 - i):
            print(j + 1, end=" ")
        print()

def main():
    print("Pattern A")
    a()
    print("Pattern B")
    b()

main()