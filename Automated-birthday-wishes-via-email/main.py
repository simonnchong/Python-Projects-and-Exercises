import smtplib
import pandas as pd
import datetime as dt
from random import choice, randint

##################### Normal Starting Project ######################

now = dt.datetime.now() # get the current datetime
today_tuple = (now.month, now.day) # get the current month and day and save into a tuple
# print(today)

data = pd.read_csv("./birthdays.csv") # read the birthday data
# print(data)

birthday_dict = {(row["month"], row["day"]) : row for (index, row) in data.iterrows()} # create a dictionary to save the data from csv
print(birthday_dict,"\n")


if today_tuple in birthday_dict: # if today date is found in the birthday dictionary
    birthday_person = birthday_dict[today_tuple] # get the birthday person value data by accessing its key
    birthday_person_name = birthday_person["name"] # get the birthday person name
    birthday_person_email = birthday_person["email"] # get the birthday person email
    # print(birthday_name, birthday_email)

    random_number = randint(1, 3) # generate a random number for choosing a letter template randomly
    print(random_number)

    with open(f"./letter_templates/letter_{random_number}.txt") as letter: # read the chosen letter template
        letter_content = letter.read() # read all contents in the letter into a string
        
    new_letter = letter_content.replace("[NAME]", birthday_person_name.strip()) # string is immutable, so replace() doesn't change the string itself but return a string instead

    # with open(f"{birthday_name}.txt", "w") as completed_letter:
    #     completed_letter.write(new_letter)

    my_email = ""
    my_password = "" # this password is only for gaining access to the Google account
    recipient_email = birthday_person_email


    # try: # check if the email send out successfully without any errors
    with smtplib.SMTP("smtp.gmail.com") as connection: # call the smtplib class, connect to Gmail SMTP server
    # Hotmail -> smtp.live.com
    # Yahoo -> smtp.mail.yahoo.com

        connection.starttls() # start TLS -> Transport Layer Security, securely connect to email server (encryption)
        connection.login(user=my_email, password=my_password) # login to your account
        connection.sendmail(from_addr=my_email, 
                            to_addrs=recipient_email, 
                            msg=f"Subject: Happy Birthday {birthday_person_name}!\n\n{new_letter}") # send the email, space 2 lines after for a content writing
    # except:
    #     print("Email sending failed")
    # else:
    #     print(f"Email has been sent to {recipient_email} successfully")

