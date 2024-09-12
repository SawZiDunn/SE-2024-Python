def split_string(x):
    splitted = x.split(",")
    for item in splitted:
        print(item.strip())
        
split_string("book,dog,drink, rain,pen")