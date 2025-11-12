def find_common_elements(list1, list2):
    result = list()
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)

    result.sort()
    return result

print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print(find_common_elements([7, 8], [9, 10]))