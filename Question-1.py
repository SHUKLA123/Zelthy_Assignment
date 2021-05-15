# Write a program that is able to send an email from the terminal to a given email address.

# Solution 1
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg['Subject'] = str(input('Enter subject of the email : '))
msg.set_content(str(input('Enter body of the email : ')))
msg['From'] = "Write_Your_Email_Id" #Example abcdef7700000000@gmail.com
msg['To'] = str(input('Enter Recipient of the email : '))

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("Write_Your_Email_Id", "Write_Your_Email_Password")
server.send_message(msg)
print('Email sent! ')
server.quit()
