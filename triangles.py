from turtle import *

speed("fastest")

for i in range(6):
    for j in range(10):
        for j in range(3):
            forward(100)
            right(120)
        right(60)
    forward(100)
    right(180)

mainloop()