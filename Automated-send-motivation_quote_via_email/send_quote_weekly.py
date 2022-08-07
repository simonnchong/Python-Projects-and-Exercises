import smtplib
import datetime as dt
from random import choice

#* ------------------------------------------------- SEND A RANDOM MOTIVATION QUOTE EVERY SUNDAY -------------------------------------------------

my_email = "your_email_here"
my_password = "your_password_here" # this password is only for gaining access to the Google account
recipient_email = "recipient_email_here"


# check today's day
now = dt.datetime.now() # get the current datetime
current_day = now.weekday()

if current_day == 6: # if today is Sunday(6)
    with open("./quotes.txt") as quotes_file: # open the file in read mode
        quote = quotes_file.readlines() # read all lines in the file and save as a list
        
    random_quote = choice(quote) # randomly choose a quote from the quote list, if choices(), this will return a list instead of an item 
    print(random_quote)


    try: # check if the email send out successfully without any errors
        with smtplib.SMTP("smtp.gmail.com") as connection: # call the smtplib class, connect to Gmail SMTP server
        # Hotmail -> smtp.live.com
        # Yahoo -> smtp.mail.yahoo.com

            connection.starttls() # start TLS -> Transport Layer Security, securely connect to email server (encryption)
            connection.login(user=my_email, password=my_password) # login to your account
            connection.sendmail(from_addr=my_email, 
                                to_addrs=recipient_email, 
                                msg=f"Subject: Be Motivated!\n\n{random_quote}") # send the email, space 2 lines after for a content writing
    except:
        print("Email sending failed")
    else:
        print(f"Email has been sent to {recipient_email} successfully")