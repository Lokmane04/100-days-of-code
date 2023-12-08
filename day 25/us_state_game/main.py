import turtle
import pandas

# reading the csv file
df = pandas.read_csv("50_states.csv")
STATES = df["state"]
x_cor = df["x"]
y_cor = df["y"]

# creating turtle to print the states
print_states = turtle.Turtle()
print_states.penup()
print_states.hideturtle()

# setting up the turtle screen

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US states game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# game loop

game_over = False
correct_answers = 0
while not game_over:
    answer = turtle.textinput(title=f"{correct_answers}/50", prompt="Guess other states name:")
    for index in range(0, len(STATES) - 1):
        if answer.lower() == STATES[index].lower():
            correct_answers += 1
            print_states.goto(x=x_cor[index], y=y_cor[index])
            print_states.write(f"{STATES[index]}")

turtle.mainloop()
