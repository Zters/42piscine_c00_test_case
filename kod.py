#!/usr/bin/env python3


import sys as s


class cc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

c1 = ""
c2 = ""


with open(s.argv[1], 'r') as fl:
	c1 = fl.read() 


with open(s.argv[2], 'r') as fl:
	c2 = fl.read()


def getch(a, b):
	if b < len(a):
		return a[b]
	else:
		return ''


def chcolor(k, color):
	return color + k + cc.ENDC


def setelem(k, c, f):
	if c < len(k):
		k[c] = f


c1l = list(c1)
c2l = list(c2)

tr='✅'
fl='❌'

i = 0


ll = max(len(c1), len(c2))

while i < ll:

	if getch(c1l, i) == getch(c2l, i): 
		setelem(c1l, i, chcolor(getch(c1, i), cc.WARNING))
		setelem(c2l, i, chcolor(getch(c2, i), cc.WARNING)) 
	else:
		setelem(c1l, i, chcolor(getch(c1, i), cc.FAIL))
		setelem(c2l, i, chcolor(getch(c2, i), cc.FAIL))
	i += 1



print(tr, ' Olması gereken\t\t', end='', sep='')
print(*c2l, sep='')
print(fl, ' Hatalı gelen  \t\t', end='', sep='')
print(*c1l, sep='')