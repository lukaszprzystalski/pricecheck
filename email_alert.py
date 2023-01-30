from email import message
import smtplib
import email_config as config
import time
import imaplib
import email
from datetime import datetime
from email.message import EmailMessage
mail_to = ''


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = config.username

    user = config.username
    password = config.password

    server = smtplib.SMTP(config.SMTP)
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

# if __name__ == '__main__':
#    email_alert('test', 'test message', mail_to)


def get_inbox():
    mail = imaplib.IMAP4_SSL(config.host)
    mail.login(config.username, config.password)
    mail.select('inbox')

    _, search_data = mail.search(None, 'UNSEEN')  # ALL, SEEN
    messages = []
    # print(search_data)

    for item in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(item, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        # print(email_message)
        for header in ['subject', 'to', 'from', 'date']:
            #print('{}: {}'.format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                # print(body.decode())
                email_data['body'] = body.decode()
            elif part.get_content_type() == 'text/html':
                body_html = part.get_payload(decode=True)
                # print(html_body.decode())
                email_data['body_html'] = body_html.decode()
        messages.append(email_data)
    return messages


def email_details(value):
    if len(get_inbox()) > 0:
        for index, item in enumerate(get_inbox()):
            print(index, item[value])
    else:
        print('there are no new emails')


if __name__ == '__main__':
    # email_details('subject')
    get_inbox()
    for item in get_inbox():
        print(item['subject'])
