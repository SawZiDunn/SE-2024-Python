def union(arr1: list, arr2: list):
    result = arr1.copy() # arr1[:]

    for i in arr2:
        if i not in result:
            result.append(i)
    return result

def intersection(arr1: list, arr2: list):
    result = []

    for i in arr1:
        if i in arr2 and i not in result:
            result.append(i)
    return result

def difference(arr1: list, arr2: list):
    result = []
    for i in arr1:
        if i not in arr2:
            result.append(i)
    return result

arr1 = [3, 1, 2, 7]
arr2 = [4, 1, 2, 5]

print(union(arr1, arr2))
print(intersection(arr1, arr2))
print(difference(arr1, arr2))