##################### Extra Hard Starting Project ######################
import pandas
from datetime import date
import random
import smtplib

my_email = "parakeet.test013@gmail.com"
password = "zutotvlxbjbnqlkx"

birthday_date = date.today()
month = birthday_date.month
day = birthday_date.day

birthdays = pandas.read_csv("birthdays.csv")

for i in range(3):
    if month == birthdays["month"][i] and day == birthdays["day"][i]:
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

        with open(file_path) as letter:
            contents = letter.read()
            final_result = contents.replace("[NAME]", birthdays["name"][i])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="macaw.test011@yahoo.com",
                                msg=f"Subject: Happy Birthday!\n\n {final_result}")

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.




