def inverse(dic: dict):
    new_dic = dict()
    for value in dic.values():

        new_list: list = [key for (key, y) in dic.items() if y == value]
        new_dic.update({value: set(new_list)})
    return new_dic

dic = {"a": "1", "b": "2", "c": "1", "d": "3", "e": "1", "f": "2"}
print(inverse(dic))