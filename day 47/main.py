import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
email = "email"
passw = "tour pass"
page_url = "https://www.amazon.in/dp/B089MS7D9K/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B089MS7D9K&pd_rd_w=3RJrU&pf_rd_p=4e9225d2-7473-4eb0-95d5-670190275218&pd_rd_wg=dcwcJ&pf_rd_r=SSJQ3YY4D88PH3AENF5S&pd_rd_r=ce63e850-ed4a-45b2-8f19-a4f1419b988a&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFPOVBaQkdDUk0yMjMmZW5jcnlwdGVkSWQ9QTAzOTAzNDUxRkRMQlJPNFg5WTNWJmVuY3J5cHRlZEFkSWQ9QTA0NDExMjAxSVU2QjY2VkZJUjExJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
response = requests.get(url=page_url,headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
                                              "Accept-Language":"en-US,en;q=0.9"})
page_data = response.text
soup = BeautifulSoup(page_data,"lxml")
current_price = float(soup.find(id="priceblock_dealprice").get_text().replace(",",'')[1:])
target_price = 70000
if current_price<=target_price:
    title = soup.find(id = "productTitle").get_text()
    message = f"subject:{title.split()[0]} Price Drop!\n\n{title}\nprice is now Rs.{current_price}\n\n{page_url}\nHurry up! ,before it run out."
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=passw)
        connection.sendmail(from_addr=email,to_addrs="akarshitgupta29@gmail.com",msg=message)

