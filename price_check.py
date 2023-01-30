from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from getpass import getpass
import config


def send_mail(subject, msg):
    try:
        server = smtplib.SMTP(config.SMTP)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.username, config.password)
        message = 'Subject: {}\n\n{}'.format(subject, website)
        server.sendmail(config.username, config.sendto, message)
        server.quit()
        print('Email succesfully sent')
    except:
        print('Email failed to send')


website = 'https://merlin.pl/lego-city-arktyczny-transport-powietrzny-60193-lego/7972441/'
subject = 'Obnizka ceny'

# open webpage and print element price
driver = webdriver.Chrome(r'C:\Users\lukasz.przystalski\Dokumenty\programowanie\python\WebDriver\chromedriver.exe')
driver.get(website)
# time.sleep(5)

# check if price is lower then requested
price = driver.find_element_by_id('product-price').text
currency = driver.find_element_by_id('product-price-currency').text
price_float = float(price.replace(',', '.'))

# send mail if  it's lower
if price_float < 100:
    print(price_float, currency)
    send_mail(subject, website)
else:
    print(price_float, currency)
driver.close()
