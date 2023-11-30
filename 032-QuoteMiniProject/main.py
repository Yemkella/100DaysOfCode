import smtplib
import datetime as dt
import random
MY_EMAIL = "REDACTED"
PASSWORD = "REDACTED"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()

if day_of_the_week == 3:
    with open("quotes.txt", "r") as file:
        list_of_quotes = file.readlines()
        quote = random.choice(list_of_quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Makes connection secure
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs="REDACTED", 
                msg=f"Subject:Quote of the week\n\n{quote}"
            )





# date_of_birth = dt.datetime(
#     year=1989,
#     month=7,
#     day=24
#     )

