#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from threading import Thread


mid    = "ucd4fc1e49365063a0cbbd693f8b1972b"
params = {"category": "square", "mid": mid)}

c = 0
def post():
    global c
    try:    requests.post("https://w.line.me/openchatactivate/api/unset", params=params)
    except: pass
    try:    requests.post("https://w.line.me/openchatactivate/api/set", params=params)
    except: pass
    c+=1
    print(c)

while True:
    Thread(target=post).start()
