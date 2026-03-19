import turtle
# Setup screen
screen = turtle.Screen()
screen.title("Car Structure using DDA and Bresenham")
screen.setup(width=600, height=600)
t = turtle.Turtle()
t.speed(0)
t.penup()
# ------------------------------
# DDA Line Drawing Algorithm
# ------------------------------
def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    steps = max(abs(dx), abs(dy))
    
    x_inc = dx / steps
    y_inc = dy / steps
    
    x = x1
    y = y1
  
    for i in range(int(steps) + 1):
        t.goto(round(x), round(y))
        t.pendown()
        t.dot(3)      # plot pixel
        t.penup()
        x += x_inc
        y += y_inc

# ------------------------------
# Bresenham’s Circle Algorithm
# ------------------------------
def draw_circle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r
    
    while x <= y:
        
        points = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ]
        
        for point in points:
            t.goto(point)
            t.pendown()
            t.dot(3)
            t.penup()
        
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
            
        x += 1

# ------------------------------
# Drawing the Car
# ------------------------------

# Rectangle Coordinates
x1, y1 = 20, 20
x2, y2 = 100, 60

# Draw Rectangle using DDA
dda(x1, y1, x2, y1)   # Bottom
dda(x2, y1, x2, y2)   # Right
dda(x2, y2, x1, y2)   # Top
dda(x1, y2, x1, y1)   # Left

# Draw Wheels using Bresenham
draw_circle(40, 10, 10)  # Left wheel
draw_circle(80, 10, 10)  # Right wheel

t.hideturtle()
screen.mainloop()


