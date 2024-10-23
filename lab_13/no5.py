
# referenced
def is_subset_total_zero(arr, result = [], sum = 0):
    if not arr: # if len(arr) == 0:
        return [result] if sum == 0 and result != [] else []
    else:
        return is_subset_total_zero(arr[1:], result + [arr[0]], sum + arr[0]) + is_subset_total_zero(arr[1:], result, sum)

        
print(is_subset_total_zero([-7, -3, -2, 5, 7]))
print(is_subset_total_zero([2, -3, 5, 8, 11, 23, -1]))