import smtplib
import datetime as dt
import pandas
import random
MY_EMAIL = "REDACTED"
PASSWORD = "REDACTED"
PLACEHOLDER = "[NAME]"
now = dt.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    name = birthday_dict[today]
    letter_number = ["1", "2", "3"]
    with open(f"./letter_templates/letter_{random.choice(letter_number)}.txt") as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace(PLACEHOLDER, name["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
            # Makes connection secure
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs="REDACTED", 
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )


