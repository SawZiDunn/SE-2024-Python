def main():
    for i in range(50):
        if i % 3 == 0:
            continue
        print(i, end=", ")

main()