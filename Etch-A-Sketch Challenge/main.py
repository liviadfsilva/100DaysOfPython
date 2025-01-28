from turtle import Turtle, Screen

zeus = Turtle()
screen = Screen()

def move_forward():
    zeus.forward(10)

def move_backward():
    zeus.back(10)

def move_counter_clockwise():
    zeus.left(10)

def move_clockwise():
    zeus.right(10)

def clear_drawing():
    zeus.clear()
    zeus.penup()
    zeus.home()
    zeus.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()