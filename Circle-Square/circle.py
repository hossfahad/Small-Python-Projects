# Circle with Squares
# A circular thing created with Python using Turtle.

import turtle

my_turtle = turtle.Turtle()
my_turtle.color('blue')
my_turtle.speed(10)

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angle)

for i in range(100):
    square(100, 90)
    my_turtle.right(11)
    
