import turtle

def draw_bar(height, char):
    width = 10
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x + 5, y - 15)
    turtle.write(char)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(width)


def char_frequency_graph():
    text = input("Enter some text: ")
    unique_chars = list()
    unique_char_count = list()
    gap = 30

    for i in text:
        if i not in unique_chars:
            unique_chars.append(i)
    for i in unique_chars:
        unique_char_count.append(text.count(i))

    turtle.left(90)
    turtle.forward(max(unique_char_count) * 20)
    turtle.backward(max(unique_char_count) * 20)
    turtle.right(90)
    
    for i in range(len(unique_chars)):
        turtle.forward(gap)
        draw_bar(unique_char_count[i] * 20, unique_chars[i])
    turtle.forward(gap)

    turtle.done()


char_frequency_graph()
