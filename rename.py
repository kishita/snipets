import sys, os, re

list = os.listdir("./")
for item in list:
	name = item.split("\n")
	p = re.compile("[0-9]+")
	regExp = p.sub("a", name[0])

	match = re.findall("[0-9]+", name[0])
	if match:
		num1 = match[0].zfill(3)
		num2 = match[1].zfill(3)
		text = "ov_comic" + num1 + "_" + num2 +".html"
		print text

	os.rename(name[0], text)