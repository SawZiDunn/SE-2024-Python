def get_the_difference(list1, list2):
    difference_list = []
    for i in list1:
        if i not in list2:
            difference_list.append(i)
            
    for i in list2:
        if i not in list1:
            difference_list.append(i)
        
    return difference_list

def main():
    list1 = [3, 1, 1, 1, 2, 7]
    list2 = [4, 1, 1, 2, 2, 5]
    print(get_the_difference(list1, list2))

main()