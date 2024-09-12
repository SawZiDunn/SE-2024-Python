import turtle, math, random

def diamond(s):
    length = s * math.sqrt(2)
    turtle.penup()
    turtle.backward(s)
    turtle.left(45)
    turtle.pendown()

    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
    turtle.right(45)
    turtle.penup()
    turtle.forward(s)
    turtle.pendown()

def cross(s):
    for _ in range(4):
        turtle.forward(s)
        turtle.backward(s)
        turtle.right(90)

def pile(s):
    cross(s / 2)
    diamond(s / 2)
    diamond(s)
    turtle.done()

def num_print():
    i = 1
    while i < 10:
        j = 1
        while j < 10:
            if i == j:
                j += 1
                continue
            print(j, end="")
            j += 1
        print()
        i += 1

def rand():
    count = int(input("How many times do you want to roll? "))
    dice_result = [0, 0, 0, 0, 0, 0]
    for i in range(count):
        result = random.randint(0, 5)
        dice_result[result] += 1
    
    for i in range(len(dice_result)):
        print(f"{i + 1} occurred {dice_result[i]} time.")


# pile(100)
# rand()
x = '\t'
print(type(x), x)