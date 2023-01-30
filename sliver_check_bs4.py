import requests
from bs4 import BeautifulSoup
import smtplib
#import config
import time
from datetime import datetime


URL_fil = r'https://www.metalmarket.eu/sw/products/monety/1-uncjowe-monety/wiedenski-filharmonik-1-uncja-srebra-2020-3938.html'
URL_eagle = r'https://www.metalmarket.eu/sw/products/monety/1-uncjowe-monety/amerykanski-orzel-1-uncja-srebra-2020-3919.html'
URL_gold_klon = r'https://www.metalmarket.eu/sw/products/monety/1-uncjowe-monety/kanadyjski-lisc-klonowy-1-uncja-zlota-2020-3899.html'
URL_kanadyjski = r'https://www.metalmarket.eu/sw/products/monety/1-uncjowe-monety/kanadyjski-lisc-klonowy-1-uncja-srebra-2020-3894.html'
URL_sil = r'https://www.coininvest.com/pl/wykresy/kurs-srebra/#chart'
URL_gold = r'https://www.coininvest.com/pl/wykresy/kurs-zlota/'

subject = 'obnika'
website = URL_fil + '\n' + URL_eagle
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}


def send_mail(subject, msg):
    try:
        server = smtplib.SMTP(config.SMTP)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.username, config.password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.username, config.sendto, message)
        server.quit()
        print('Email succesfully sent')
    except:
        print('Email failed to send')


def check_price(link, nazwa, klasa):
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # send mail if  it's lower
    if nazwa == 'filharmonik':
        price = soup.find(id='projector_price_value').get_text().split()
        converted_price = float(price[0].replace(',', '.'))
        if converted_price < 78.0:
            send_mail(subject, URL_fil)
            print('Email has been sent')
        else:
            print(nazwa, converted_price)
    elif nazwa == 'kanadyjski':
        price = soup.find(id='projector_price_value').get_text().split()
        converted_price = float(price[0].replace(',', '.'))
        if converted_price < 76.0:
            send_mail(subject, URL_kanadyjski)
            print('email has been sent')
        else:
            print(nazwa, converted_price)
    elif nazwa == 'eagle':
        price = soup.find(id='projector_price_value').get_text().split()
        converted_price = float(price[0].replace(',', '.'))
        if converted_price < 80.0:
            send_mail(subject, URL_eagle)
            print('Email has been sent')
        else:
            print(nazwa, converted_price)
    elif nazwa == 'klon':
        price = soup.find(id='projector_price_value').get_text().split()
        converted_price = (price[0]+price[1]).replace(',', '.')
        converted_price = float(converted_price)
        if converted_price < 6350.0:
            send_mail(subject, URL_gold_klon)
            print('Email has been sent')
        else:
            print(nazwa, converted_price)
    elif nazwa == 'silver':
        price = soup.find(class_=klasa).get_text().split()
        converted_price = float(price[0].replace(',', '.'))
        if converted_price < 62.0:
            send_mail(subject, URL_sil)
            print('Email has been sent')
        else:
            print(nazwa, converted_price)
    elif nazwa == 'gold':
        # print(price)
        price = soup.find(class_=klasa).get_text().split()
        converted_price = (price[0]+price[1]).replace(',', '.')
        converted_price = float(converted_price)
        # print(converted_price)
        if converted_price < 6150.0:
            send_mail(subject, URL_gold)
        else:
            print(nazwa, converted_price)



print(datetime.now())
check_price(URL_fil, 'filharmonik', '')
check_price(URL_eagle, 'eagle', '')
check_price(URL_kanadyjski, 'kanadyjski', '')
check_price(URL_gold_klon, 'klon', '')
check_price(URL_sil, 'silver', 'live_metal_prices_li_txt')
check_price(URL_gold, 'gold', 'live_metal_prices_li_txt')
print('')

