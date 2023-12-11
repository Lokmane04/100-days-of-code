import math
from tkinter import *

window = Tk()

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 *60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
REPS = 1
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    if REPS == 8:
        count_down(LONG_BREAK_MIN)
        canvas.itemconfig(timer_text, text="")
        title.config(text=f"you did it 🥳 🥳", fg=RED, font=(FONT_NAME, 20, "bold"))
        return 0
    elif REPS % 2 == 0:
        title.config(text=f"take a break 😊", fg=PINK, font=(FONT_NAME, 17, "bold"))
        count_down(SHORT_BREAK_MIN)
    else:
        title.config(text=f"time to work", fg=GREEN, font=(FONT_NAME, 20, "bold"))
        count_down(WORK_MIN)
    REPS += 1


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            mark += '✔'
            check_text.config(text=f"{mark}", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 20, "bold"))


def reset_timer():
    global REPS, TIMER
    REPS = 1
    window.after_cancel(TIMER or '')
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    check_text.config(text='')

# ---------------------------- UI SETUP ------------------------------- #


window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", bg=PINK, font=(FONT_NAME, 10, "bold"), command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", bg=PINK, font=(FONT_NAME, 10, "bold"), command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_text = Label(text="", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
check_text.grid(column=1, row=3)
window.title("Pomodoro")

window.mainloop()
