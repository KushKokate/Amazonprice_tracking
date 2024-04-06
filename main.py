import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

sender_mail = 'kokatekush96@gmail.com'
receiver_mail = sender_mail
app_password = 'pfnq kbsn nwer wbsl'

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,fr;q=0.6'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

price_element = soup.find(class_='a-price-whole')
if price_element:
    price = price_element.getText()
    number = int(float(price))

    if number >= 95:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_mail, app_password)
            server.sendmail(to_addrs=receiver_mail, from_addr=sender_mail,
                            msg=f'Subject : Hey! the prices just dropped\n\n The price of the cooker is {number} and you can it here {url}')
        print("email sent successfully")
    else:
        print("Price is below $95")
else:
    print("Price information not found on the webpage.")
