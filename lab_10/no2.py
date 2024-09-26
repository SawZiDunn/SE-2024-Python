def remove_the_thirds(list1: list):
    index = 2 # start from the first third element
    while index < len(list1):
        list1.pop(index)
        index += 2

def main():
    list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
    remove_the_thirds(list1)
    print(list1)

main()