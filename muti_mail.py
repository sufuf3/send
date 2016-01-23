# -*- coding:utf8 -*-
import csv, sys
import smtplib
import email
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = '<enter-gmail-username>'
password = '<enter-gmail-password>'
smtpserver = 'smtp.gmail.com:587'

def sendemail():
    sender = "<enter-gmail-address>"
    s = smtplib.SMTP(smtpserver)
    s.starttls()
    s.login(username, password)
    
    f = open('mail.csv', 'r')    #recipient's email save form csv file at first column
    for row in csv.reader(f):
        recipient = row[0]
    
        msg = MIMEMultipart('alternative')
        msg['Subject'] = u"嗨Hello"
        msg['From'] = sender
        msg['To'] = recipient

        html = """\
            <html>
            <head></head>
                <body>This is a email test message.
                </body>
            </html>
            """
        part = MIMEText(html, 'html', 'utf-8')
    
        msg.attach(part)
        problems = s.sendmail(sender, reciver, msg.as_string())

    s.quit()    

def main():
    sendemail()

if __name__ == "__main__":
	main()

# Now you have to access follow these link and login by sender account.
# https://www.google.com/settings/security/lesssecureapps
# https://accounts.google.com/DisplayUnlockCaptcha
