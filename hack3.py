import os

print("stating traffic")

i = 65

while (i <= 122):
	osname = "iamhacker3_mtabishkk"+chr(i)
	url = "http://192.168.1.23/cgi-bin/startdocker.py?osname={}&ostype=ubuntu%3A14.04".format(osname)
	cmd = 'curl "{}"'.format(url)
	os.system(cmd)
	i = i + 1

print("100 traffic send")