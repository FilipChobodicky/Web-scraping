import requests
from bs4 import BeautifulSoup
import login_details 

secure_url = ('https://the-internet.herokuapp.com/secure')
login_url = ('https://the-internet.herokuapp.com/authenticate')

payload = {
    'username': login_details.username,
    'password': login_details.password
}

# r = requests.post(login_url, data=payload)
# print(r.text)
# r2 = requests.get(secure_url)
# print(r2.text)

with requests.session() as s:
    # r = s.post(login_url, data=payload)
    # print(r.text)
    s.post(login_url, data=payload)
    r = s.get(secure_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())
