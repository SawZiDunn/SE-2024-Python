def list_member(key, arr):
    if not arr: return False

    if arr[0] == key:
        return True
    else:
        return list_member(key, arr[1:])


print(list_member(3, [1, 2, 3, 5]))