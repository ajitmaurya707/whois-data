import whois
import webbrowser as wb
from json2html import *

w = whois.whois('https://www.google.com')
d = json2html.convert(json = w)

f = open("index.html","w")
w = f.write(d)
f.close()
wb.open("index.html")
