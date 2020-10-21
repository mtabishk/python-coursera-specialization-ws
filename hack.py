import os

print("stating traffic")

i = 1
osname = "hacker_tabish"+chr(i)
while (i < 3):
	osname = "hacker_tabish"+chr(i)
	os.system('curl "http://192.168.1.23/cgi-bin/startdocker.py?osname={}&ostype=ubuntu%3A14.04"'.format(osname))
	i = i + 1

print("100 traffic send")