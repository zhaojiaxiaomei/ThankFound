#Author: zxz
import requests
from login import getToken
import json
def getData(sale_no):
    url='http://172.7.0.202:3000/auth/setting/info'
    url1='http://172.7.0.202:3000/customers/customers/listpage'
    data={"page_size":100,"page_no":1,"order_column":"","order_by":"","condition":{"customer_no":"","customer_name":"","identity_no":"","mobile":"","parent_name":"","parent_no":"","sales_no":sale_no,"sales_name":"","start_time":"","end_time":""}}
    cookies={'token':getToken()}
    #print(getToken())
    result = requests.post(url1,json=data,cookies=cookies)
    js=result.json()
    datas=json.loads(js["datas"])
    return datas

if __name__ == '__main__':
    print(getData('S60001629'))