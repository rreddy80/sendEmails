#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header    import Header
from email.mime.text import MIMEText
from getpass         import getpass
from smtplib         import SMTP_SSL
import smtplib

login, password = 'email@gmail.com', 'emailPassword'
recipients = ['receipientsemail@gmail.com']

# create message
msg = MIMEText('message body…', 'plain', 'utf-8')
msg['Subject'] = Header('subject…', 'utf-8')
msg['From'] = login
msg['To'] = ", ".join(recipients)

# send it via gmail
s = smtplib.SMTP('smtp.googlemail.com', 587)
s.ehlo()
s.starttls()
s.ehlo
s.set_debuglevel(1)
try:
    s.login(login, password)
    s.sendmail(msg['From'], recipients, msg.as_string())
except smtplib.SMTPException:
    print("smtplib.SMTPException: No suitable authentication method found.")
except smtplib.SMTPAuthenticationError:
    print("Username, password combination does not match. Please check and try again!")
except:
    print(sys.exc_info()[:2])
    print("Unknown exception found, please contact support.!")
finally:
    s.quit()
