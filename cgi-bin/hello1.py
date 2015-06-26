#!/usr/bin/env python3
import urllib as urllib2

c=urllib.urlopen('http://www.google.ru/')
contents=c.read()
print("Content-type: text/html")
print()
print("<h1>Hello world!</h1>")
print(contents[0:50])
