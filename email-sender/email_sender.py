import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import sys


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Python'
email['to'] = sys.argv[1]
email['subject'] = 'Python generated mail just for the sake of practice please ignore'

email.set_content(html.substitute({'name': sys.argv[2]}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pythonpy113@gmail.com', 'thug auuy dtzd fxri')

    smtp.send_message(email)
    print('All good')