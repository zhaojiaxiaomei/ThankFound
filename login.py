#Author: zxz
import requests
from lxml import html
import re
USERNAME = "13703213368"
PASSWORD = "zxz123"

LOGIN_URL = "http://172.7.0.202:3000/login/signup"

def getToken():
    session_requests = requests.session()
    payload = {
        "user_name": USERNAME,
        "password": PASSWORD,
    }
    result = session_requests.post(LOGIN_URL, data=payload)
    re_token=re.match('.*?:\"(.*?)\"}',result.json()["datas"])
    with open('a.txt','w') as fp:
        fp.write(re_token.group(1))
    return re_token.group(1)

if __name__ == '__main__':
    respone=getToken()
    print(respone)