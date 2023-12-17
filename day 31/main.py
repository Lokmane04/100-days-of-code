from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ----------------- UI SETUP-----------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)


canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))

canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

window.mainloop()