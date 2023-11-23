import smtplib
import datetime as dt
import random
import os

MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(MY_EMAIL, MY_PASSWORD)
        server.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject:Monday Motivation\n\n{quote}")

# import smtplib
#
# sender = "Person <from@example.com>"
# receiver = "A Test User <to@example.com>"
#
# message = f"""\
# Subject: Hello
# To: {receiver}
# From: {sender}
#
# This is a test e-mail message."""
#
# with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
#     server.login("*******", "*********")
#     server.sendmail(sender, receiver, message)

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1995, month=12, day=10)
# print(date_of_birth)
#
# print(day_of_week)
