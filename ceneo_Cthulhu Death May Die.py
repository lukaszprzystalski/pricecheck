from email import message
# from turtle import title
import requests
from bs4 import BeautifulSoup
import smtplib
import email_config as config
import time
from datetime import datetime
from email.message import EmailMessage
mail_to = ''
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}


def email_alert(time, subject, body, to):
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


URL = r'https://www.ceneo.pl/93666169;pla?se=YxWbm1iqQxdyrhZALD2q02WnsAqEsNg5&shop=146599877&gclid=EAIaIQobChMI7aaBrMmZ_AIVC4nICh3SBg9HEAQYASABEgKFxvD_BwE'


def check_price(link, pricecheck: float):
    # print(25 * '*')
    now = datetime.today()
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        title = soup.find(
            class_='product-top__product-info__name js_product-h1-link js_product-force-scroll js_searchInGoogleTooltip default-cursor').get_text()
        print(title)
    except Exception as err:
        print(err)
    try:
        price = soup.find(class_='value').get_text()
        subprice = soup.find(class_='penny').get_text()
        fullprice = price + subprice
        fullprice = fullprice.replace(',', '.')
        print(fullprice)
    except Exception as err1:
        print(err1)

    # check price and send email
    try:
        if float(fullprice) < float(pricecheck):
            email_alert(now, 'obnizka Cthulhu: Death May Die: ' +
                        str(fullprice), link, mail_to)
            print('email sent')
        else:
            print(now)
    except Exception as error4:
        print(error4)


if __name__ == '__main__':
    while True:
        check_price(URL, 320)
        print('')
        print('...czekamy...')
        print('')

        time.sleep(3600)
