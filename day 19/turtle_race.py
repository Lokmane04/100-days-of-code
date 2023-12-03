import random
from turtle import Screen, Turtle

game_over = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "blue", "green", "orange", "purple", "yellow", "brown", "gray"]
turtles = []

user_bet = screen.textinput(title='Turtle Race', prompt='Which turtle is going to win the race !! :')


def choose_turtles():
    for turtle_index in range(0, len(colors)):
        new_turtle = Turtle("turtle")
        new_turtle.color(colors[turtle_index])
        turtles.append(new_turtle)


def position_turtles_for_race():
    y_axis = -60
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x=-230, y=y_axis)
        y_axis += 30


def turtle_race():
    global game_over
    for turtle in turtles:
        if turtle.xcor() >= 220:
            game_over = True
            if user_bet == turtle:
                print(f"You won 🥳 🥳 , The  winner is {turtle.pencolor()}")
            else:
                print(f"You lost 🥲 🥲 , The  winner is {turtle.pencolor()}")

        turtle.forward(random.randint(0, 10))


def game():
    choose_turtles()
    position_turtles_for_race()
    while not game_over:
        turtle_race()


game()
screen.exitonclick()
