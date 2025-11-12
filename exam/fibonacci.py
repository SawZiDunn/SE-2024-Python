def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    f0 = 0
    f1 = 1
    for i in range(2, n + 1):
        current_fibonacci = f0 + f1
        f0 = f1
        f1 = current_fibonacci
    return current_fibonacci


# print(fibonacci_iterative(5))
print(fibonacci_recursive(5))