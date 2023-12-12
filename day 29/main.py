from tkinter import *

window = Tk()
window.title("Password manager")
window.config(pady=50, padx=50)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    with (open("passwords.txt", mode='a') as file):
        file_text = f"\n\nwebsite : {website_entry.get()}\nusername/email : {username_entry.get()}\npassword: {password_entry.get()}\n\n\n________________"
        file.write(file_text)
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        password_entry.delete(0, END)


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

username_entry = Entry(width=55)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "red@gmail.com")

password_entry = Entry(width=55)
password_entry.grid(column=1, row=3, columnspan=2)

# Buttons

generate_button = Button(text="Generate password", width=15)
generate_button.grid(column=2, row=4, columnspan=1)

add_button = Button(text="Add to library", command=save_password)
add_button.grid(column=1, row=4, columnspan=1)

window.mainloop()
