def char_frequency():
    text = input("Enter some text: ")
    unique_chars = list()
    unique_char_count = list()

    for i in text:
        if i not in unique_chars:
            unique_chars.append(i)
    for i in unique_chars:
        unique_char_count.append(text.count(i))
    
    print("-- Character Frequency Table --")
    print("char percentage (character count / string length)")

    for i in range(len(unique_chars)):
        char_percentage = (unique_char_count[i] / len(text)) * 100
        print(f"{unique_chars[i]}\t{char_percentage:.2f}%")

char_frequency()
