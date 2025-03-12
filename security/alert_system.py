import smtplib
from email.mime.text import MIMEText

def send_alert():
    sender = "your_email@gmail.com"
    receiver = "alert_email@gmail.com"
    subject = "Security Alert: Motion Detected"
    body = "Motion has been detected by the night patrolling robot."

    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail(sender, receiver, msg.as_string())

    print("Email alert sent!")
