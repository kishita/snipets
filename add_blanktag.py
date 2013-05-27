import sys, os, re

list = os.listdir("./")
for item in list:
	name = item.split("\n")

	fp = open(name[0])
	fp2 = open("../" + name[0], "w")
	for line in fp.readlines():
		match = re.search("<a href=\"http://.*\"><img", line)

		if match:
			text = match.group(0)[:-5] + " target=\"_blank\">"
			new_text = text + "<img" + line[int(match.end()):]
			fp2.write("\t\t" + new_text)
		else:
			fp2.write(line)

	fp.close()
	fp2.close()