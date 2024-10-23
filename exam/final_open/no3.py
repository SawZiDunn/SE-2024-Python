def count_operands_in_expr(exp):
    # if type(exp) != tuple:
    if not isinstance(exp, tuple):
        return 1
    
    # or
    # if not isinstance(exp, int):
    # if type(exp) is int:
    #     return 1
    
    return count_operands_in_expr(exp[0]) + count_operands_in_expr(exp[2])

exp = ((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4)) 
print(count_operands_in_expr(exp))