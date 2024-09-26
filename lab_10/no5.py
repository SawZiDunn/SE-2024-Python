def merge(list1, list2):

    merged_list = list1 + list2
    # bubble sort algorithm
    for i in range(len(merged_list)):
        for j in range(len(merged_list) - i - 1):
            if merged_list[j] > merged_list[j + 1]:
                merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j] # swap
    return merged_list

def main():
    # list1 = input("Enter List1: ").split(" ")
    # list2 = input("Enter List2: ").split(" ")

    list1 = [1, 5, 16, 61, 111]
    list2 = [2, 4, 5, 6]

    print("The merged list is ", end="")
    for i in merge(list1, list2):
        print(i, end=" ")
    print()

main()

