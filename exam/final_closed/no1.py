def find_word_positions(word, list_of_words):
    result = list()
    for i in range(len(list_of_words)):
        if word.lower() == list_of_words[i].lower():
            result.append(i)
    
    return result if len(result) > 0 else 0

def main():
    print(find_word_positions("Python",["python","Java", "c", "python", "prolog"]))
    print(find_word_positions("iOS",["window", "macOS", "Linx"]))

main()