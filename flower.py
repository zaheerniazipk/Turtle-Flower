# Project : Flower Shape using Turtle

# Basic Setup
# pip install turtle  (Mostly pre-installed with Python)

# import turtle library
import turtle                       # Allows us to use turtles

# make turtle object
t = turtle.Turtle()

t.shape()                           # Set the Pen Shape like Turtle, Square
t.pensize(1)                        # Set the Pen/ Arrow Size

# Make window/screen object
sc = turtle.Screen()                # Creates a playground for turtles
sc.setup(900,800)                   # Set the Window Size
sc.title("Turtle Flower")           # Set the window title    

# Color Properties
sc.bgcolor('white')
t.pencolor('green')

# Pen Fast Speed
t.speed(10)                         # Fastest 0, Fast 10, Normal 6 , Slow 1

# number of circles
n = 20

# Loop for printing circles in Flower Shape
for i in range(n):
    t.circle(190-1, 90)             
    t.left(98)                      # Move to the left Direction

    t.circle(190-1, 90)
    t.left(18)

turtle.done()
sc.mainloop()                       # Wait for user to close window