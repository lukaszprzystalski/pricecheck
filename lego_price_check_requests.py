from email import message
import requests
from bs4 import BeautifulSoup
import smtplib
import email_config as config
import time
from datetime import datetime
from email.message import EmailMessage
from requests_html import HTML

now = datetime.now()
year = now.year

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


def url_to_txt(url, filename='file.html', save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f'plik-{year}.html', 'w') as f:
                f.write(html_text)
        return html_text
    else:
        html_text = r.text
    return html_text


url = r'https://www.amazon.pl/LEGO-Creator-Sklep-zabawkami-31105/dp/B07W4KTR2V/'

html_text = url_to_txt(url)
# print(html_text)

r_html = HTML(html=html_text)

table_class = '#priceblock_ourprice_row'
r_table = r_html.find(table_class)
print(r_html.absolute_links)
