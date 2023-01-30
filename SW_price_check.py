import requests
from bs4 import BeautifulSoup
import smtplib
import time
from datetime import datetime


URL = r'https://www.cdkeys.com/pc/games/star-wars-jedi-fallen-order-pc-en?utm_source=daisycon&utm_medium=cpa&utm_campaign=www.pepper.pl&utm_content=daisycon'

subject = 'obnizka'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

tekst = soup.find(class_='price').get_text()

print(tekst)