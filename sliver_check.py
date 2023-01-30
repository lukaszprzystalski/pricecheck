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


website = r'https://www.metalmarket.eu/sw/products/monety/1-uncjowe-monety/wiedenski-filharmonik-1-uncja-srebra-2020-3938.html'
subject = 'filharmonik'

# open webpage and print element price
path = '/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)
# time.sleep(5)

# check if price is lower then requested
price = driver.find_element_by_id('projector_price_value').text.split()
price_float = float(price[0].replace(',', '.'))
currency = price[1]
#print(price_float, currency)

# send mail if  it's lower
if price_float < 80:
    print(price_float, currency)
    send_mail(subject, website)
else:
    print(price_float, currency)
driver.close()
