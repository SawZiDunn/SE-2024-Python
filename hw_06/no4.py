number_to_word = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def num_to_word(x):
    
    if x < 0 or x > 999:
        return "I don't know."
    elif x < 21:
        return number_to_word[x] if x != 0 else ""
    elif 21 <= x <= 99:
        tens = x - (x % 10)
        ones = x % 10
        return number_to_word[tens] + '-' + number_to_word[ones]
    else: # 100 <= x <= 999
        and_or_not = " and " if (x % 100) != 0 else ""
        return number_to_word[x // 100] + " hundred" + and_or_not + num_to_word(x % 100)

x = int(input("Enter a number: "))
print(num_to_word(x))
