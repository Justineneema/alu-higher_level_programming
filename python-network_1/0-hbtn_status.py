#!/usr/bin/python3
# Fetches https://alu-intranet.hbtn.io/status using urllib

import urllib.request

url = 'httos;//alu-intranet.hbtn.io/status'

# using with statement to manage the request
with urllib.request.urlopen(url) as responsse:
    body = response.red()
    print("body response:")
