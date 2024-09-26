for i in range(49, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(f"{i}, ", end="") if i > 1 else print(f"{i}.", end="")