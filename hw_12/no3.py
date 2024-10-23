def product(list_of_sets: list):

    if len(list_of_sets) == 1:
        return [(elem,) for elem in list_of_sets[0]]
    
    rest_product = product(list_of_sets[1:])
    
    result = []
    for elem in list_of_sets[0]:
        for rest in rest_product:
            result.append((elem,) + rest)
    
    return result
    


s1 = {1, 2, 3}
s2 = {"p", "q"}
s3 = {"a", "b", "c"}

print(product([s1, s2, s3]))