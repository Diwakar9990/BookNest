import eventlet

from celery import Celery
from celery.schedules import crontab
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

eventlet.monkey_patch()
sender_mail = "urdaddy9922@gmail.com"
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = sender_mail
smtp_password = 'tgllmquoxycxznqn'  
cel = Celery('tasks', broker='redis://127.0.0.1:6379')
cel.conf.enable_utc = False
cel.conf.timezone = 'Asia/Kolkata'


@cel.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Send a weekly reminder to return books every Friday at 10:00 AM
    sender.add_periodic_task(
        # crontab(day_of_week='fri', hour=10, minute=0),
        crontab(hour=12, minute=19),
        send_return_reminder.s()
    )

@cel.task
def send_return_reminder():
    subject = "Weekly Reminder: Please Return Your Book"
    message = "This is a friendly reminder to return your borrowed book by the due date."
    # for user in users:
    send_email(sender_mail, 'yitofa9531@foraro.com', subject, message)

def send_email(sender, recipient, subject, message):
    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = recipient
    msg['subject'] = subject
    msg.attach(MIMEText(message))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, recipient, msg.as_string())
