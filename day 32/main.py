import smtplib

my_email = 'baslilokmane04@gmail.com'
app_password = 'dhfeseigwtnhaava'
reciever = 'lokmanbas999@gmail.com'
message = "Subject:Quote by Marcus Aurelius\n\nWhen you arise in the morning think of what a privilege it is to be alive, to think, to enjoy, to love..."
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()

connection.login(user=my_email, password=app_password)
connection.sendmail(from_addr=my_email, to_addrs=reciever, msg=message)
connection.close()