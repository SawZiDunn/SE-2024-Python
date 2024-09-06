def sum_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

print("The sum of all digits:", sum_digits(100))