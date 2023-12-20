import smtplib
from datetime import datetime as dt
import pandas
import random

today = (dt.now().month, dt.now().day)

# you should change the email and the password
MY_EMAIL = 'baslilokmane04@gmail.com'
PASSWORD = 'dhfeseigwtnhaava'

df = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (i, row) in df.iterrows()}

letter_num = random.randint(1, 3)
if today in birthdays_dict:
    reciever = birthdays_dict[today]

    with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
        letter = letter_file.readlines()
        letter[0] = letter[0].replace("[NAME]", f"{reciever["name"]}")
        letter = ''.join(letter)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Birthday motivation\n\n{letter}")