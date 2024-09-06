import turtle

#constant variables
days_each_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_start = [1, 4, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0]
days_each_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

table_length = 250
box_width = table_length / 7
box_height = table_length / 10

def move_down(x):
    turtle.right(90)
    turtle.forward(x)
    turtle.left(90)

def draw_box(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def draw_calendar():
    turtle.speed(0)
    month = int(input("Month of the year: "))

    # draw heading
    draw_box(table_length, box_height)

     # write month name
    turtle.penup()
    x, y = turtle.position()
    turtle.goto(x + 75, y - 20)
    turtle.write(f"{months[month - 1]} 2024", align="left", font=("Ariel", 10, "normal"))
    turtle.goto(x, y)
    turtle.pendown()

    # to the lower row
    move_down(box_height)

    day_count = 1 # for printing days
    for row in range(7):
        for col in range(7):
            draw_box(box_width, box_height)

            # draw day row
            if row == 0:
                turtle.penup()
                x, y = turtle.position()
                turtle.goto(x + 8, y - 20)
                turtle.write(days_each_week[col], align="left", font=("Ariel", 10, "normal"))
                turtle.goto(x, y)
                turtle.pendown()

            else:
                if (row >= 2 or col + 1 >= day_start[month - 1]) and day_count <= days_each_month[month - 1]:
                    turtle.penup()
                    x, y = turtle.position()
                    turtle.goto(x + 25, y - 20)
                    turtle.write(day_count, align="right", font=("Ariel", 10, "normal"))
                    turtle.goto(x, y)
                    turtle.pendown()
                    day_count += 1
            turtle.forward(box_width)
           
        turtle.backward(table_length)
        move_down(box_height)

    turtle.done()

draw_calendar()
    


    
    