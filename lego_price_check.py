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


# URL1 = r'https://www.amazon.pl/LEGO-Star-mrocznych-szturmowc%C3%B3w-75324/dp/B09BNV1HRL/ref=sr_1_1?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=PVX3J33V42D6&keywords=lego+75324&qid=1662375323&sprefix=lego+75324%2Caps%2C119&sr=8-1'
# URL2 = r'https://www.amazon.pl/LEGO-75301-My%C5%9Bliwiec-Skywalkera-elementy/dp/B08G4GP34B/ref=sr_1_1?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2K30IB9BCOZHX&keywords=lego+75301&qid=1662375465&sprefix=lego+75301%2Caps%2C94&sr=8-1'
# URL3 = r'https://www.amazon.pl/LEGO-My%C5%9Bliwiec-Obi-Wana-Kenobiego-75333/dp/B09QFXRYYH/ref=d_pd_sbs_sccl_2_10/259-6015543-9074632?pd_rd_w=wo9nb&content-id=amzn1.sym.4dc5f9e6-4066-4442-a95d-8b1961394968&pf_rd_p=4dc5f9e6-4066-4442-a95d-8b1961394968&pf_rd_r=5158C24S0X7PKV2HNNBH&pd_rd_wg=zqhSx&pd_rd_r=86619df9-7491-4555-a085-e4130d714c81&pd_rd_i=B09QFXRYYH&psc=1'
# URL4 = r'https://www.amazon.pl/dp/B08G4H3SQG/?tag=pk0d5d-21'
URL9 = r'https://www.amazon.pl/717376-001-716724-421-716724-1C1-HSTNN-DB4R-HSTNN-IB4R/dp/B07VXWCGTJ/ref=asc_df_B07VXWCGTJ/?tag=plshogostdde-21&linkCode=df0&hvadid=504275520227&hvpos=&hvnetw=g&hvrand=11317311804008011433&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1011536&hvtargid=pla-1392075881736&psc=1'
URL5 = r'https://www.amazon.pl/dp/B08WWTPDG2?tag=ugcplpepper21-21&ascsubtag=0v004n2vt8sd'
URL7 = r'https://www.amazon.pl/LEGO-75344-Mikromy%C5%9Bliwiec-Regulowane-Mandalorian/dp/B0BBRZ7XSX/ref=sr_1_1?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2C0W4F8LGG8H9&keywords=75344&qid=1672655068&sprefix=75344%2Caps%2C121&sr=8-1'
# URL = r'https://www.amazon.pl/LEGO-Creator-Sklep-zabawkami-31105/dp/B07W4KTR2V/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}


def check_price(link, pricecheck: float):
    # print(25 * '*')
    now = datetime.today()
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        title = soup.find(id='productTitle').get_text().strip()
        print(title)
    except Exception as err:
        print(err)
    try:
        price = soup.find(class_='a-offscreen').get_text().replace(',', '.')
        price = float(price[:-2])
        print(price)
    except Exception as err1:
        print(err1)

    # check price and send email
    try:
        if float(price) < float(pricecheck):
            email_alert(now, 'obnizka lego: ' + str(price), link, mail_to)
            print('email sent')
        else:
            print(now)
    except Exception as error4:
        print(error4)


if __name__ == '__main__':
    while True:
        # check_price(URL1, 95)
        # check_price(URL2, 160)
        # check_price(URL3, 110)
        # check_price(URL4, 25)
        check_price(URL5, 140)
        # check_price(URL9, 160)
        check_price(URL7, 35)
        print('')
        print('...czekamy...')
        print('')

        time.sleep(3600)
