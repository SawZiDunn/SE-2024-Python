import random

x = random.randint(0, 3)
y = int(input("Scissor(0), Rock(1), Paper(2): "))
if y < 0 or y > 2:
    print("Must be from 0 to 2!")

if x == 0:
    if y == 0:
        print("The computer is scissor. You are scissor. It's a draw.")
    if y == 1:
        print("The computer is scissor. You are rock. You won.")
    if y == 2:
        print("The computer is scissor. You are paper. You lose.")
elif x == 1:
    if y == 0:
        print("The computer is rock. You are scissor. You lost.")
    if y == 1:
        print("The computer is rock. You are rock. It's a draw")
    if y == 2:
        print("The computer is rock. You are paper. You won")
else:
    if y == 0:
        print("The computer is paper. You are scissor. You won")
    if y == 1:
        print("The computer is paper. You are rock. You lost.")
    if y == 2:
        print("The computer is paper. You are paper. It's a draw")
