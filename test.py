# import pyperclip
# pyperclip.copy("You'r account has been hacked")
# pyperclip.paste
# print(None)

import bs4
import requests

res = requests.get('https://www.google.com')
res.raise_for_status()
text = bs4.BeautifulSoup(res.text,'html.parser')
print(type(text))