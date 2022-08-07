import smtplib
import datetime as dt

#* ------------------------------------------------- SEND EMAIL -------------------------------------------------

my_email = "your_email_here"
my_password = "your_password_here" # this password is only for gaining access to the Google account
recipient_email = "recipient_email_here"


try:
    with smtplib.SMTP("smtp.gmail.com") as connection: # call the smtplib class, connect to Gmail SMTP server
    # Hotmail -> smtp.live.com
    # Yahoo -> smtp.mail.yahoo.com

        connection.starttls() # start TLS -> Transport Layer Security, securely connect to email server (encryption)
        connection.login(user=my_email, password=my_password) # login to your account
        connection.sendmail(from_addr=my_email, 
                            to_addrs=recipient_email, 
                            msg="Subject: Hello Simon\n\nThis is the content of email")
except:
    print("Email sending failed")
else:
    print("Email has been sent successfully")


#! if you encountered this error, like so 
#  raise SMTPAuthenticationError(code, resp)
# smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials n14-20020a170902d2ce00b0016cbb46806asm6513208plc.278 - gsmtp')

# you need go to your email setting
#* turn off these settings:
# --- Use your phone to sign in
# --- 2-Step Verification

#* and you need to have 2-step verification setting then get the app password







#* ------------------------------------------------- PRACTICING DATETIME MODULE -------------------------------------------------

now = dt.datetime.now() # get the current datetime

print(now)
# 2022-08-07 21:31:53.760751

print(now.year) # integer type today is year 2022
# 2022

print(now.month) # integer type today is August
# 8

print(now.day) # integer type, today is 7th
# 7

print(now.time())
# 21:44:10.336723

print(now.weekday()) # return the current day in integer, Monday - Sunday (0 - 6), 7 days, start from 0
# 6 # this means today is Sunday