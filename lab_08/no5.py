def LCS(s1, s2):
    x = len(s1)
    y = len(s2)
    final_temp = ""
    
    for i in range(x):
        for j in range(y):
            temp = ""
            count = 0
            while (i + count < x) and (j + count < y) and s1[i + count] == s2[j + count]:
                temp += s1[i + count]
                count += 1
            if len(temp) > len(final_temp):
                final_temp = temp

    return final_temp

print(LCS("ingenious", "intelligent"))
print(LCS("condition", "fictional"))
print(LCS("smart", "meter"))
print(LCS("front-end", "back-end"))
print(LCS("philosophically", "zoophilous"))
print(LCS("abc", "def"))

