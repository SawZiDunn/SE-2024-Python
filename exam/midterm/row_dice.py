import random

def rand():
    count = int(input("How many times do you want to roll? "))
    dice_result = [0, 0, 0, 0, 0, 0]
    for i in range(count):
        result = random.randint(0, 5)
        dice_result[result] += 1
    
    for i in range(len(dice_result)):

        
        print(f"{i + 1} occurred {dice_result[i]} time.")