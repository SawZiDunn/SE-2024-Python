def num_print():
    i = 1
    while i < 10:
        j = 1
        while j < 10:
            if i == j:
                j += 1
                continue
            print(j, end="")
            j += 1
        print()
        i += 1