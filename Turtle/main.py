from turtle import *

def square(t, size):
    for l in range(4):
        t.forward(size)
        t.left(90)

def triangle(t, size):
    for l in range(3):
        t.forward(size)
        t.left(120)
        
        
ask = input("Square or Triangle? ").lower()
t = Turtle()

while ask != "quit":
    if ask == "square":
        size = int(input("Enter the size: "))
        square(t, size)
    elif ask == "triangle":
        size = int(input("Enter the size: "))
        triangle(t, size)
    else:
        print("Shape not present")
    ask = input("Square or Triangle? ").lower()