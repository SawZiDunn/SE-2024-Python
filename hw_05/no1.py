def square_root(n, loop):
    guess = n / 2
    for i in range(loop):
        temp = n / guess
        guess = (guess + temp) / 2
    return guess

def main():
    n = float(input("n: "))
    a = square_root(n, 5)
    b = square_root(n, 6)
    c = square_root(n, 7)

    print(f"Square root of n is {a:.3f}.")
    print(f"Square root of n is {b:.3f}.")
    print(f"Square root of n is {c:.3f}.")

main()