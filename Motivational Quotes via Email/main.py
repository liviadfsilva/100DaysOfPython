import smtplib
import datetime as dt
import random

my_email = "parakeet.test013@gmail.com"
password = "zutotvlxbjbnqlkx"

message = random.randint(0, 102)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("quotes.txt") as quotes:
        chosen_quote = quotes.readlines()[message]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="macaw.test011@yahoo.com",
                            msg=f"Subject: Good Morning!\n\n {chosen_quote}")