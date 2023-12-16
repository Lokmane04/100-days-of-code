import json
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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    json_data = {
        website: {  # if website is a variable
            "email": email,
            "password": password
        }
    }
    if website and email and password:

        save = messagebox.askokcancel(title=website,
                                      message=f"These are the details entered :\nemail : {email}\npassword: {password}\nis it ok to save ? ")

        if save:

            try:
                with open("passwords.json", mode='r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(json_data)

                with open("passwords.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        else:
            messagebox.showinfo(title="Oops", message="Please fill up all the fields :)")


# ---------------------------- search for password ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "red@gmail.com")

password_entry = Entry(width=40)
password_entry.grid(column=1, row=3)

# Buttons

search_button = Button(text="Search", width=15,command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate password", width=15, command=generate_password)
generate_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add to library", command=save_password, width=36)
add_button.grid(column=1, row=4)

window.mainloop()
