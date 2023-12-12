from tkinter import *
from tkinter import messagebox
from password_generator import random_password_generator
import pyperclip

window = Tk()
window.title("Password manager")
window.config(pady=50, padx=50)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)  # This will clear the entry
    PASSWORD = random_password_generator()
    password_entry.insert(0, PASSWORD)
    pyperclip.copy(PASSWORD)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    if website_entry.get() and email_entry.get() and password_entry.get():

        save = messagebox.askokcancel(title=website_entry.get(),
                                      message=f"These are the details entered :\nemail : {email_entry.get()}\npassword: {password_entry.get()}\nis it ok to save ? ")
        if save:
            with (open("passwords.txt", mode='a') as file):
                file_text = f"\nwebsite : {website_entry.get()}\nemail : {email_entry.get()}\npassword: {password_entry.get()}\n________________"
                file.write(file_text)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please fill up all the fields :)")


# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=200)

mypass_image = PhotoImage(file="logo.png")

canvas.create_image(120, 100, image=mypass_image)
canvas.grid(column=1, row=0)
# Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Username/Email: ")
username_label.grid(column=0, row=2)

password_label = Label(text="Password : ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "red@gmail.com")

password_entry = Entry(width=55)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons

generate_button = Button(text="Generate password", width=15, command=generate_password)
generate_button.grid(column=2, row=4, columnspan=1)

add_button = Button(text="Add to library", command=save_password)
add_button.grid(column=1, row=4, columnspan=1)

window.mainloop()
