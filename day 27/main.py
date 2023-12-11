from tkinter import *


def convert_miles_to_km():
    km_result_label.config(text=f"{round(int(miles_input_field.get()) * (1609 / 1000))}")


window = Tk()

window.config(padx=50, pady=50)
title = window.title("Mile to km converter")

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

miles_input_field = Entry(width=15)

miles_input_field.grid(column=1, row=0)

miles_text = Label(text='miles')
miles_text.grid(column=2, row=0)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)


km_text = Label(text='km')
km_text.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)
window.mainloop()
