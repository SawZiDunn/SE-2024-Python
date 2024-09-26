def check_substring(x, y):
    
    for i in range(len(y) - len(x) + 1):
        temp = ""
        for j in range(len(x)):
            temp += y[j + i]
        if temp == x:
            return f"\'{x}\' is a substring of {y}."
            
    return f"\'{x}\' is not a substring of {y}."

print(check_substring("how are you?"," you"))
print(check_substring("you","how are you"))