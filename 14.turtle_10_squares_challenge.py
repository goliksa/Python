import turtle

def square(step):
    for side in range(0, 4):
        turtle.forward(step)
        turtle.right(90)

count = 0
go = 6
step = 4

while count != 10:
    square(go)
    turtle.penup()
    turtle.goto(step*-1, step)
    turtle.pendown()
    count += 1
    go += 8
    step += 4
    print(count)

