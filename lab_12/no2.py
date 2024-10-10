def find_duplicates(dic: dict):
    new_dict = {}
    for (key, value) in dic.items():
        # dic.values() returns an obj that contains all the values in dic
        # it doesn't return a list
        # so we convert it to a list, to use count() method
        
        value_list = list(dic.values())
        if value_list.count(value) > 1:
            new_dict[key] = value
    return new_dict
    

myDict = {"s5301": "Fred", "s5302": "Harry", "s5303": "John", "s5304": "Fred", "s5305": "Harry"}

print(find_duplicates(myDict))

