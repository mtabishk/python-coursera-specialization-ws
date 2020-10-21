#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

print("<html>")
print("<head><title>Output</title></head>")
print("<body>")
print("<pre>")

form = cgi.FieldStorage()

command = form.getvalue("choice")

cmd = "{}".format(command)
output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]


if status == 0:
    query = out
    import os
    import datetime

    def greetme():
        currenth = int(datetime.datetime.now().hour)
        if 0 <= currenth < 12:
            print('<center><h2>Good Morning !</h2><center>')

        if 12 <= currenth < 16:
            print('<center><h2>Good Afternoon !</h2></center>')

        if 16 <= currenth < 19:
            print('<center><h2>Good Evening !</h2></center>')

        if currenth >= 19 and currenth != 0:
            print('<center><h2>Good Night !</h2></center>')

    greetme()


    if ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ( ("chrome" in query) or ("browser" in query) ):
        print( sp.getoutput("chrome &") )

    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and (("notepad" in query) or ("gedit" in query)):
        print(  sp.getoutput("gedit &"))

    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("firefox" in query):
        print( sp.getoutput("firefox &"))

    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("calender" in query):
        print("""<b>"""+sp.getoutput("cal")+"""</b>""")

    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ("date" in query):
        print("""<b>"""+ sp.getoutput("date")+ """</b>""")

    elif ( ("start" in query) or ("open" in query) or ("run" in query) or ("execute" in query) or ("begin" in query) ) and ( ("cmd" in query) or ("terminal" in query) ):
        print( sp.getoutput("gnome-terminal"))

    elif ( ("status" in query)  and ("docker" in query)):
        print("""<b>"""+sp.getoutput("docker ps")+"""</b>""")

    else:
        print()
        print()
        print('<center><b>Command not found... Try again...</b></center>')

else:
    print()
    print()
    print("<center><h2>Invalid Command</h2><center>")


print("</pre>")
print("</body>")
print("</html>")
