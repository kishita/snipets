# -*- coding: utf-8 -*-

import pickle, urllib, os
url = "http://www.pythonchallenge.com/pc/def/banner.p"
pick = urllib.urlopen(url).read()
f = open("pickle.txt","w")
f.write(pick)
f.close()
f = open("pickle.txt","r")
tmp = pickle.load(f)
os.remove("pickle.txt")
print tmp
for i in tmp:
	law = ""
	for x, y in i:
		law += x*y
	print law