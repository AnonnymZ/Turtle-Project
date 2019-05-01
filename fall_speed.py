from turtle import *
import time
import math
bob = Turtle()
i = 0
nb = 0
x = 0
h = int(input())
bob.home()
bob.right(-90)
bob.home()
while i < h+10:
    i = i + 1
    bob.forward(10)
    if h >= 50:
        if i%10 == 0:
            bob.write(i, font=("Arial", 8, "normal"))
    else:  
        if i%5 == 0:
            bob.write(i, font=("Arial", 8, "normal"))
bob.write("  M/S", font=("Arial", 15, "normal"))
bob.home()
bob.right(-90)
while x < h+10:
    x = x + 1
    bob.forward(10)
    if h >= 50:
        if x%10 == 0:
            bob.write(x, font=("Arial", 8, "normal"))
    else:  
        if x%5 == 0:
            bob.write(x, font=("Arial", 8, "normal"))
bob.write("  M", font=("Arial", 15, "normal"))
bob.home()
for w in range(0,h):
    result = math.sqrt(9.8*2*w)
    bob.goto(result*10,w*10)
    bob.color("red")
if h >= 50:
    i = screensize()
    print(i[0]+i[1])
    screensize(i[0]+h*100/4,i[1]+h*100/4)
