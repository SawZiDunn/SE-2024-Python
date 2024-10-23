abbreviations = {
    "be": "b",
    "because": "cuz",
    "see you": "cu",
    "see": "c",
    "the": "da",
    "okay": "ok",
    "are": "r",
    "you": "u",
    "without": "w/o",
    "why": "y",
    "ate": "8",
    "great": "gr8",
    "mate": "m8",
    "wait": "w8",
    "later": "l8r",
    "tomorrow": "2mro",
    "for": "4",
    'before': "b4",
    "once": "1ce",
    "and": "&",
    "your": "ur",
    "you're": "ur",
    "as far as I know": "afaik",
    "as soon as possible": "asap",
    "at the moment": "atm",
    "be right back": "brb",
    "by the way": "btw",
    "for your information": "fyi",
    "in my humble opinion": "imho",
    "in my opinion": "imo",
    "laugh out loud": "lol",
    "oh my god": "omg",
    "roll on the floor laughing": "rofl",
    "talk to you later": "ttyl"
}

def textese(s):
    splitted_strs = s.split(" ")
    result = list()
    for string in splitted_strs:
        if string in abbreviations:
            result.append(abbreviations[string])
        else:
            result.append(string)

    return " ".join(result)

def untextese(s):
    splitted_strs = s.split(" ")
    result = list()
    for string in splitted_strs:
        for (key, value) in abbreviations.items():
            if string == value:
                result.append(key)
                break
        # for else => else will only when the loop is finished
        # if the loop breaks before finishing, else block will not work
        else:
            result.append(string)

    return " ".join(result)

print(textese("oh my god, Jim, are you okay ?"))
print(untextese("oh my god, Jim, r u ok ?"))


