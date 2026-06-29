Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# SLICING
# POSITIVE SLICING
a = "codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
b = "work until you succeed"
b[:4]
'work'
>>> b[5:10]
'until'
>>> b[11:14]
'you'
>>> b[15:22]
'succeed'
>>> c = "codegnan it solution"
>>> c[9:11]
'it'
>>> c[:8]
'codegnan'
>>> c[12:20]
'solution'
>>> # NEGATIVE SLICING
>>> d = "vijayawada is a royal city"
>>> d[-10:-5]
'royal'
>>> d[-26:-16]
'vijayawada'
>>> d[-4:0]
''
# "0" CANN'T BE USED AT LAST
>>> d[-4:]
'city'
>>> e = "vizag is city of destiny"
>>> e[-15:-11]
'city'
>>> e[-24:-19]
'vizag'
>>> e[-7:]
'destiny'
