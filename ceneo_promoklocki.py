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
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


URL1 = r'https://promoklocki.pl/lego-star-wars-75344-mikromysliwiec-kosmiczny-boby-fetta-p22181'
URL2 = r'https://promoklocki.pl/lego-star-wars-75347-bombowiec-tie-p22179#264614'
URL3 = r'https://promoklocki.pl/lego-star-wars-75345-zestaw-bitewny-zolnierze-klony-z-501-legionu-p22180'
URL4 = r'https://promoklocki.pl/lego-city-60384-pingwinia-furgonetka-ze-slushem-p22143'


def check_price(link, pricecheck: float):
    # print(25 * '*')
    now = datetime.today()
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    alldata = soup.find(
        class_='row m-0').get_text().strip().split()
    # print(alldata)
    try:
        dataForEmail = soup.find_all(class_='col-6 col-lg-7')
    except Exception as err:
        print(err)
    title = dataForEmail[0].get_text()
    price = dataForEmail[5].get_text().split()[0].replace(',', '.')
    print(title)
    print(price)

    # check price and send email
    try:
        if float(price) < float(pricecheck):
            email_alert(now, 'Boba Fett\'s Starship Microfighter: ' +
                        str(price), link, mail_to)
            print('email sent')
        else:
            print(now)
    except Exception as error4:
        print(error4)


if __name__ == '__main__':
    while True:
        # check_price(URL1, 35.00)
        # print('')
        check_price(URL2, 200.00)
        print('')
        check_price(URL3, 70.00)
        print('')
        check_price(URL4, 55.00)
        print('')
        print('...czekamy...')
        print('')

        time.sleep(3600)
