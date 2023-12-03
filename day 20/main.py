from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# creating the turtle object
starting_position=[(0,0),(-20,0),(-40,0)]


for position in starting_position:
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(position)





screen.exitonclick()
