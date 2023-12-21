from tkinter import *
import requests


# fetching the quote

def fetch_quote():
    response = requests.get(url="https://api.kanye.rest")
    # raising exception
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    return quote


def get_quote():
    quote = fetch_quote()
    canvas.itemconfig(quote_text, text=f"{quote}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)

background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# fixing the ui for the first time the window gets rendered
first_quote = fetch_quote()
quote_text = canvas.create_text(150, 207, text=f"{first_quote}", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
