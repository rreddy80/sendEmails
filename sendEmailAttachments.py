"""
Author:     Ramesh Reddy
Date:       23/Oct/2015
Purpose:    Send an email with the given attachment to a list of pre-defined
            list of recepients
Change History:
----------------------------------------------------------------------------
Date        Author      Description
----------------------------------------------------------------------------

"""
from zipfile import ZipFile
import glob, os, sys
import smtplib, datetime
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

address_book = ['ramesh.reddy@companyname.com']
send_from = 'ramesh.reddy@companyname.com'
subject = "Automated EMail: xyz Result(s) on {0}".format(datetime.datetime.now())
#print(subject)
text = """Please do not respond this email.

Your email id is part of the group who are opted in to automated emails as soon as regression runs. Please talk to me, if you do not wish to receive these emails.

Regards

"""
os.chdir('C:\\xyz\\')
pyfiles = glob.glob("*.csv")
txtfiles = glob.glob("*.txt")
logfiles = glob.glob("*.log")
pyfiles.extend(txtfiles)
pyfiles.extend(logfiles)
#print pyfiles

def send_mail(send_from, send_to, subject, text, files=None,
              server='exchange.companyName.com'):
    assert isinstance(send_to, list)

    msg = MIMEMultipart(
        From=send_from,
        To=COMMASPACE.join(send_to),
        Date=formatdate(localtime=True),
        Subject=subject
    )
    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            msg.attach(MIMEApplication(
                fil.read(),
                Content_Disposition='attachment; filename="%s"' % basename(f),
                Name=basename(f)
            ))

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


newf = "{0}_{1}.zip".format(sys.argv[1], sys.argv[2])

with ZipFile(newf, 'w') as wf:
    for filename in pyfiles:
        wf.write(filename)
        
gFile = [newf]
try:
    send_mail(send_from, address_book, subject, text, files=gFile)
except:
    send_mail(send_from, address_book, subject, text, files=None)
