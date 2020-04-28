# web browser Comes with Python and opens a browser to a specific page.
#
# requests Downloads files and web pages from the internet.
#
# bs4 Parses HTML, the format that web pages are written in.
#
# selenium Launches and controls a web browser.
# The selenium module is able to fill in forms and simulate mouse clicks in this browser

import webbrowser,sys,pyperclip

if len(sys.argv)>1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
