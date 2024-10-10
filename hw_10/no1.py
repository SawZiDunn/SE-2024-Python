import turtle

def pie_chart(list1: list):
    radius = 100
    list1.sort()
    unique_nums = list()
    unique_nums_count = list()
    for i in list1:
        if i not in unique_nums:
            unique_nums.append(i)
    for i in unique_nums:
        unique_nums_count.append(list1.count(i))

    turtle.circle(radius)
    turtle.left(90)
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()

    total = sum(unique_nums_count)
    
    for i in unique_nums_count:
       
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(360 * (i / total))

    turtle.done()
    

def main():
    list1 = [3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3]
    
    pie_chart(list1)

main()