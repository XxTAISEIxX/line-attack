#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from threading import Thread


mid    = ""
params = {"category": "square", "mid": mid)}

c = 0
def post():
    try:    requests.post("https://w.line.me/openchatactivate/api/unset", params=params)
    except: pass
    try:    requests.post("https://w.line.me/openchatactivate/api/set", params=params)
    except: pass
    c+=1
    print(c)

while True:
    Thread(target=post).start()
