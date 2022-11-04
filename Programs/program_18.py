# Program to send email using SMTP

import smtplib
from email.message import EmailMessage

URI = "smtp.gmail.com"


def send_email(
    sender_email: str,
    sender_password: str,
    receiver_email: str,
    subject: str,
    message: str,
):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(message)
    with smtplib.SMTP_SSL(URI, 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)


if __name__ == "__main__":
    sender_email = input("Enter sender email: ")
    sender_password = input("Enter sender password: ")
    receiver_email = input("Enter receiver email: ")
    subject = input("Enter subject: ")
    message = input("Enter message: ")
    send_email(sender_email, sender_password, receiver_email, subject, message)
    print("Email sent successfully")
