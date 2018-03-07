import turtle

for side in range(0, 100):
    turtle.forward(10)
   # if side !=3:        # without last turn
    turtle.right(side + 3.14)

print('done')
