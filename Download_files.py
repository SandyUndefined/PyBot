import requests

res = requests.get('https://en.wikipedia.org/wiki/Tester')
res.raise_for_status()
playFile = open('test.txt','wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)

playFile.close()