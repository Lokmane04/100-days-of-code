from tkinter import *

def clicked():
    text['text'] = "i got clicked"

window = Tk()

window.minsize(width=600,height=400)

title = window.title("First GUI program")


text = Label(text='Some text .')
text.pack()
button = Button(text="Click me",command=clicked)
button.pack()

window.mainloop()