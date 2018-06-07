#Author: zxz
import requests
import json
with open('a.txt','r') as fp:
    Token = fp.read()

def getData(sale_no):
    url1 = 'http://172.7.0.202:3000/customers/customers/listpage'
    dicts = {'customer_no': '', 'customer_name': '', 'identity_no': '', 'mobile': '', 'parent_name': '',
             'parent_no': '', 'sales_no': sale_no, 'sales_name': '', 'start_time': '', 'end_time': ''}
    data = {'page_size': 100, 'page_no': 1, 'order_column': '', 'order_by': '',
            'condition': dicts}
    strs = json.dumps(data)
    cookies = {'token': Token.strip()}
    print(strs)
    result = requests.post(url1, data={"data": strs}, cookies=cookies)
    print(result.status_code)
    js = result.json()
    print(js)
    datas = json.loads(js["datas"])
    return datas

if __name__ == '__main__':
    print(getData('S60001629'))