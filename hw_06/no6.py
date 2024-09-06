def reverse(x):
    result = ""
    for i in str(x):
        result = i + result

    return int(result)

print(reverse(3456))