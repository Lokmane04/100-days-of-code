from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")


# ----------------- UI SETUP-----------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

right_img = PhotoImage(file="images/right.png")
known_word_button = Button(image=right_img, highlightthickness=0, command=next_card)
known_word_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
unknown_word_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_word_button.grid(row=1, column=0)
unknown_word_button = Button()

window.mainloop()
