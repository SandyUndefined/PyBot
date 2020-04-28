import requests,bs4

res = requests.get('https://www.google.com')
res.raise_for_status()