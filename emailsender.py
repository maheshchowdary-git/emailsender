import random
import smtplib
from email.message import EmailMessage


user_mail = input("Enter target's gmail: ")
username = input("Enter your mail id:")
password = input("Enter your mail password: ")
subject = input("Enter subject: ")
message = input("Enter message: ")
def gmail_otp():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = user_mail
    s.login(username, password)
    s.send_message(msg)
    s.quit()

number_of_mails = int(input("Enter how many times you want to send the mail : "))
i=0
while(i < number_of_mails):
    gmail_otp()
    i += 1


