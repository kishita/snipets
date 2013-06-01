# -*- coding: utf-8 -*-

import urllib,re
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
seed = '8022'
for i in range(400):
	text = urllib.urlopen(url+seed).read()
	print text
	seed = "".join(re.findall(r"nothing is (\d+)", text))
	print seed
	try :
		int(seed)
		print " Next:", seed
	except :
		print " Last:", text
		break