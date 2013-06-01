# -*- coding: utf-8 -*-

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
import string
value = string.ascii_lowercase[2:]+string.ascii_lowercase[:2]
key = string.ascii_lowercase
maps = dict(zip(key, value))
print "".join([maps.get(c,c) for c in text])
