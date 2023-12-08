import time
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
states_not_guessed=[]
game_over = False
correct_answers = []
while not game_over:
    if len(correct_answers) > 50:
        print_states.home()
        print_states.write(f"Congrats , You Won !! 🥳 ", align="center", font=("Arial", 45, "normal"))
        time.sleep(3)
        break

    answer = turtle.textinput(title=f"{len(correct_answers)}/50", prompt="Guess other states name:")
    if answer.lower() == 'exit':
        break
    for index in range(0, len(STATES) - 1):
        if answer.lower() == STATES[index].lower():
            correct_answers.append(STATES[index])
            print_states.goto(x=x_cor[index], y=y_cor[index])
            print_states.write(f"{STATES[index]}")

for state in STATES:
    if state not in correct_answers:
        states_not_guessed.append(state)
df = pandas.DataFrame(states_not_guessed)
df.to_csv("states_to_learn.csv")
# you won't find any states to learn because i know them all xd
