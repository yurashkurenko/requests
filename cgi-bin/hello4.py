#!/usr/bin/env python3
import requests
r=requests.get('http://yandex.ru',)
print("<!DOCTYPE html")
print(r.text)
