import turtle as t
from random import randint

win = t.Screen()
win.title("Circle of circles")
t.speed("fastest")
for i in range(36):
    for i in range(36):
        t.forward(10)
        t.right(10)
    t.forward(20)
    t.right(10)

t.mainloop()
