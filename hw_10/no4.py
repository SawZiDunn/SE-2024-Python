def print_table(arr: list):
    for inner_arr in arr:
        for j in inner_arr:
            print(j, end="\t")
        print()
    print()

list1 = [
    ["X", "Y"],
    [0, 0],
    [10, 10],
    [200, 200]
]

print_table(list1)

list2 = [
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
]
print_table(list2)