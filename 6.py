import urllib, os

url = "http://www.pythonchallenge.com/pc/style.css"
#url = "http://www.pythonchallenge.com/pc/def/channel.html"
tmp = urllib.urlopen(url).read()
print tmp
