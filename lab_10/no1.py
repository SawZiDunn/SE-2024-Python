def name_list():
    result = list()
    count = 1
    while True:
        name = input(f"Enter name {count}: ")
        if name:
            result.append(name)
            count += 1
        else:
            break
    return result

print(name_list())