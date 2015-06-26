#!/usr/bin/env python3
import requests
r=requests.get('https://github.com/yurashkurenko',auth=('yurasoft@mail.ru','finger1972'))
print("Content-type: text/html")
print(r.text)
