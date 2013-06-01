f = open("url.txt", "r")
#print f.readlines()
l = f.readlines()
r = []
for w in l:
	r.append(w.split("\n")[0])

print r
print r.index("236")
print r.index("236", 64, 200)
tmp = [r.count(el) for el in r]
print tmp
print tmp.count(1)

g = open("url_2.txt", "w")
for i in range(46):
	g.write(r[i] + "\n")