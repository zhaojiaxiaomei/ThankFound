#Author: zxz
import xlwt
import time
from math import floor
from getInfo import getData
import json
def inits(datas):
    items=datas["items"]
    for item in items:
        item['interest'] = 0
        item['commission'] = 0
        item['getcom'] = 0
        item['now_balance'] = 0
    return items
def GenerateInterest(it):
    item=[]
    for i in it:
        temp = i['balance_total']
        i['interest'] = floor((temp*0.099)/365)
        item.append(i)
    return item
def GenerateCommission(it,sale_no):
    item=[]
    item2=[]
    pdict={}
    adict={}
    #将有子节点的父节点生成dict
    for i in it:
        if i['parent_no']==None:
            pass
        else:
            for j in it:
                if j['customer_no']==i['parent_no']:
                    pdict[j['customer_no']] = j['balance_total']
                    continue
    #计算佣金
    for i in it:
        temp = i['interest']
        if i['parent_no']==sale_no:
            i['commission']=floor(temp*0.3)
        elif i['parent_no']==None:
            i['commission']=0
        else:
            if pdict[i['parent_no']] >= 50000000:
                i['commission'] = floor(temp * 0.3)
            elif pdict[i['parent_no']] >= 30000000:
                i['commission']=floor(temp*0.25)
            elif pdict[i['parent_no']] >= 25000000:
                i['commission']=floor(temp*0.2)
            elif pdict[i['parent_no']] >= 15000000:
                i['commission']=floor(temp*0.15)
            elif pdict[i['parent_no']] >= 5000000:
                i['commission'] = floor(temp*0.1)
            else:
                i['commission'] = floor(temp * 0.05)
        item.append(i)
    ls = list(pdict.keys())
    #将佣金加到
    for j in ls:
        adict[j]=0
        for i in it:
            if i['parent_no']==j:
                adict[j]=adict[j]+i['commission']
    print(adict)
    for i in item:
        if i['customer_no'] in ls:
            i['getcom'] = adict[i['customer_no']]
        item2.append(i)
    return item2

def newBlance(it):
    item=[]
    for i in it:
        i['now_balance']=i['balance_total']+i['interest']+i['getcom']
        item.append(i)
    return item
def GenerateRate(it):
    rate=0
    for i in it:
        rate=floor(i['getcom']*0.3)+rate
    return rate

def writeExcel(it,rate,sales_no):
    file = xlwt.Workbook(encoding='ascii')
    sheet = file.add_sheet('My Worksheet', cell_overwrite_ok=True)
    headList = ['mobile', 'customer_no', 'parent_no', 'balance_total', 'interest', 'commission', 'getcom',
                'now_balance']
    sheet.write(0,0,'手机号')
    sheet.write(0,1,'客户号')
    sheet.write(0,2,'邀请人编号')
    sheet.write(0,3,'以前资金')
    sheet.write(0,4,'获得利息')
    sheet.write(0,5,'上交的佣金')
    sheet.write(0,6,'得到佣金')
    sheet.write(0,7,'最新余额')
    for i in range(1, it.__len__()+1):
        for j in range(0, headList.__len__()):
            sheet.write(i, j, label=it[i-1][headList[j]])
    sheet.write(i + 2, 0, sales_no)
    sheet.write(i+2,1,'提成')
    sheet.write(i+2,2,rate)
    now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
    file.save(now +'_'+sales_no+'.xls')

if __name__ == '__main__':
    sales_no = 'p60001635'
    datas=getData(sales_no)
    items=inits(datas)
    print(items)
    item=GenerateInterest(items)
    it=GenerateCommission(item,sales_no)
    its=newBlance(it)
    rate=GenerateRate(its)
    writeExcel(it,rate,sales_no)