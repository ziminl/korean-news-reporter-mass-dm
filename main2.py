


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def send_emails():



    sender_email = 'gmail'
    subject = 'title of mass dm!'
    message = 'test message'

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = 'gmail'  
    password = 'password'



    with open('recipients.csv', 'r') as file:
        reader = csv.reader(file)
        recipients = [row[0] for row in reader]

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        for recipient_email in recipients:
            msg['To'] = recipient_email
            server.send_message(msg)
    print('sent')

if __name__ == '__main__':
    send_emails()


