import smtplib
from email.message import EmailMessage
from string import Template  # allows for eas substitution of variables in a string
from pathlib import Path

html =Template(Path('index.html').read_text())
email = EmailMessage()
email['from']='michael.arnold.316@outlook.com'
email['to']='michael.arnold.316@outlook.com'
email['subject'] = 'You won $1,000,000'

email.set_content(html.substitute(name='Mike'), 'html')

with smtplib.SMTP(host='', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('username','password')
  smtp.send_message(email)

