def list_reverse(arr):
    if len(arr) <= 1:
        return arr
    else:
        return arr[-1:] + list_reverse(arr[:-1])

print(list_reverse([1, 2, 3, 4, 5]))