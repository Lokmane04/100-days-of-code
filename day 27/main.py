from tkinter import *


def clicked():
    text.config(text=f"{input_field.get()}")


window = Tk()

window.minsize(width=500, height=300)

title = window.title("First GUI program")

text = Label(text='Some text .')
text.grid(column=0, row=0)

input_field = Entry(width=15)

input_field.grid(column=3,row=0)

button = Button(text="Click me", command=clicked)
button.grid(column=2,row=1)

new_button = Button(text="new button", command=clicked)
new_button.grid(column=4,row=4)

window.mainloop()
