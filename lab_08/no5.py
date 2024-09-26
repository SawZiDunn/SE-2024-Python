def LCS(s1, s2):
    x = len(s1)
    y = len(s2)
    final_substring = ""

    for i in range(x):
        for j in range(y):
            count = 0
            temp_str = ""
            while i + count < x and j + count < y and s1[i + count] == s2[j + count]:
                temp_str += s2[j + count]
                count += 1
            if len(temp_str) > len(final_substring):
                final_substring = temp_str
    return final_substring


print(LCS("ingenious", "intelligent"))
print(LCS("condition", "fictional"))
print(LCS("smart", "meter"))
print(LCS("front-end", "back-end"))
print(LCS("philosophically", "zoophilous"))
print(LCS("abc", "def"))

