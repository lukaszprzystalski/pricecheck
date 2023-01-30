import requests
from bs4 import BeautifulSoup
import smtplib
import email_config as config
import time
from datetime import datetime

URL = r'https://store.steampowered.com/app/1075190/A_Game_of_Thrones_The_Board_Game__Digital_Edition/'

subject = 'obnika'
website = URL + '\n'
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

def check_price(link, klasa):
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # send mail if  it's lower
    price = float(soup.find(class_='game_purchase_price price').get_text().split()[0][:-2].replace(',', '.'))
    if price < 80.0:
        send_mail(subject, URL)
        print('Email has been sent')
    else:
        print(price)
    
print(datetime.now())
check_price(URL, '')

print('')

