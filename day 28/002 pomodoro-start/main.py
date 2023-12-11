from tkinter import *

window = Tk()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    print("start")

def reset_timer():
    print("reset")

# ---------------------------- UI SETUP ------------------------------- #


window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

title = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="start", command=reset_timer)
reset_button.grid(column=2, row=2)

check_text = Label(text="✔")
check_text.grid(column=1, row=3)
window.title("Pomodoro")

window.mainloop()
