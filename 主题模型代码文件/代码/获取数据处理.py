import openpyxl
import pandas as pd
import xlrd
from collections import Counter
import pandas as pd
# coding=utf-8

def duqu(shuzi):
    sheet = xlrd.open_workbook('D:\desktop\科研训练\数据/31000.xls')
    sheet_names = sheet.sheet_names()
    for sheet_name in sheet_names:
        sheet = sheet.sheet_by_name(sheet_name)
        cols = sheet.col_values(shuzi)
        print(cols[0])
        cols.pop(0)
        return cols
def chuli():
    df = pd.DataFrame()
    zhuanlihao = duqu(1)
    biaoti = duqu(2)
    zhaiyao = duqu(3)
    ipc = duqu(4)
    shijian = duqu(5)
    wenben = []
    time = []
    zhaiyao1 = []
    for i in zhaiyao:
        biaozhi = 'USE -'
        try:
            head, sep, tail = i.partition(biaozhi)
            linshi0 = head.replace('DESCRIPTION OF DRAWING(S) -','')
            linshi1 = linshi0.replace('DETAILED DESCRIPTION - INDEPENDENT CLAIMS','')
            linshi2 = linshi1.replace('NOVELTY -','')
            linshi3 = linshi2.replace('USE -','')
            linshi4 = linshi3.replace('ADVANTAGE -','')
            linshi5 = linshi4.replace('3D','Three dimensional')
            linshi6 = linshi5.replace('DETAILED DESCRIPTION - An INDEPENDENT CLAIM','')
            linshi7 = linshi6.replace('"', '')
        except:
            linshi0 = i.replace('DESCRIPTION OF DRAWING(S) -', '')
            linshi1 = linshi0.replace('DETAILED DESCRIPTION - INDEPENDENT CLAIMS', '')
            linshi2 = linshi1.replace('NOVELTY -', '')
            linshi3 = linshi2.replace('USE -', '')
            linshi4 = linshi3.replace('ADVANTAGE -', '')
            linshi5 = linshi4.replace('3D', 'Three dimensional')
            linshi6 = linshi5.replace('DETAILED DESCRIPTION - An INDEPENDENT CLAIM', '')
            linshi7 = linshi6.replace('"', '')
        zhaiyao1.append(linshi7)
    for i in range(len(biaoti)):
        a = biaoti[i]+'\n'+zhaiyao1[i]
        wenben.append(a)
    for i in shijian:
        b = i.split(' ')
        try:
            time.append(b[5])
        except:
            time.append('none')
    df['专利号'] = zhuanlihao
    df['文本'] = wenben
    df['ipc'] = ipc
    df['时间'] = time
    df.to_excel("专利31000.xlsx", index=False)
chuli()
def tongji():
    sheet = openpyxl.load_workbook('D:\desktop\科研训练\数据/专利31000.xlsx')
    sheet1 = []
    mySheet = sheet.get_sheet_by_name('Sheet1')
    col = mySheet["D"]
    for cell in col:
        a = cell.value
        sheet1.append(a)
    sheet1.pop(0)
    result = pd.DataFrame()
    #result['ciyu'] = sheet1
    linshi = pd.value_counts(sheet1)
    #result.to_excel('nianfentongji.xlsx',index=False)
    print(type(linshi))
    print(list(linshi.index))
    print(list(linshi.values))

#tongji()
