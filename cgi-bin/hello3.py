#!/usr/bin/env python3
import requests
r=requests.get('http://brain.cx/',)
print("Content-type: text/html")
print(r.text)
