import gspread

import os

from email.mime.text import MIMEText

import smtplib, ssl

from pathlib import Path

# importing and setting variables and blah blah blah
sa = gspread.service_account()
sh = sa.open("Head New Accountability")
wks = sh.worksheet("Training Accountability")
account = wks.get('A2:C24')
absent = []

# if cell is empty then I grab email
for i in account:
    val = i[1]
    if val == '':
        absent.append(i[2])

# beginning SMTP magic
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
subject = "FILL OUT HEAD NEW ACCOUNTABILITY"
body = Path('email.txt').read_text()
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
send_email(subject, body, EMAIL_ADDRESS, absent, EMAIL_PASSWORD)

print("Done!")