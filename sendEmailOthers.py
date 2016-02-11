import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

emailfrom = email_From
emailto = email_To
fileToSend = <<file_to_send>>
username = <<userName>>
password = <<passWord>>


msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "help I cannot send an attachment to save my life"
msg.preamble = "help I cannot send an attachment to save my life"

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)
#AUTH_PLAIN = "PLAIN"


if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

# send it via gmail
s = smtplib.SMTP('exchange.company.com', 25, timeout=10)
s.ehlo()
s.starttls()
s.ehlo
s.set_debuglevel(1)
try:
    s.login(username, password)
    s.sendmail(emailfrom, emailto, msg.as_string())
except smtplib.SMTPException:
    print("smtplib.SMTPException: No suitable authentication method found.")
except smtplib.SMTPAuthenticationError:
    print("Username, password combination does not match. Please check and try again!")
except:
    print(sys.exc_info()[:2])
    print("Unknown exception found, please contact support.!")
finally:
    s.quit()

