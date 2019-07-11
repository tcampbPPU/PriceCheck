import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'ENTER_URL_TO_AMAZON_ITEM'

headers = {"User-Agent": "ENTER_YOUR_USER_AGENT"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


    title = soup2.find(id="productTitle").get_text()

    priceString = soup2.find(id="priceblock_ourprice").get_text().strip().replace('$', '')

    price = float(priceString)

    if(price < ): # enter some amount
        # send notification
        send_email()

    print(title.strip(), price)

def send_email():
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login("GMAIL_EMAIL", "GMAIL_PASSWORD")

        subject = 'Price is low'

        body = 'Click the link \n' # add the link to item here

        message = f"Subject: {subject}\n\n{body}"

        s.sendmail("TO", "FROM", message)

        s.quit()
        print('Email Sent')
    except:
        print('Something went wrong')



check_price()
