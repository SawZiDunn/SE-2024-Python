def conversion():
    while True:
        x: str = input("Enter an integer: ")
        if x.isdigit() or (x.startswith("-") and x[1:].isdigit()):
            break
    x = int(x)
    
    if x == 0:
        print(f"It is {x}. I quit.")
    elif x < 0:
        print(f"It is {x}, a negative integer. I quit.")
    else:
        bin_str = int_to_bin_str(x)
        print("Converting int to binary string: ", bin_str)
        print("Converting binary string back to integer: ", bin_str_to_int(bin_str))

def int_to_bin_str(x: int):
    bin_str = ""
    while x != 0:
        bin_str = str(x % 2) + bin_str
        x = x // 2
    return bin_str
        
def bin_str_to_int(x: str):
    total = 0
    for (index, i) in enumerate(x[::-1]):
        if i == '1':
            total += 2 ** index
        
    return total
    
conversion()