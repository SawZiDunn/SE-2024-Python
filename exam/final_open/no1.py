def find_member_positions(number, list_of_numbers):
    return_list = list()
    for i in range(len(list_of_numbers)):
        if number == list_of_numbers[i]:
            return_list.append(i)

    return 0 if len(return_list) == 0 else return_list


print(find_member_positions(2, [2, 5, 3, 2, 4]))
print(find_member_positions(1, [2, 5, 3, 2, 4]))