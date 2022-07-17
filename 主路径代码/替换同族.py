import os
import re

import pymysql

conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_final')
cur = conn.cursor()

path="E:\科研训练\patent"
files=os.listdir(path)
txts=[]
for file in files: #遍历文件夹
    position = path+'\\'+ file #构造绝对路径，"\\"，其中一个'\'为转义符
    print(position)
    with open(position, "r",encoding='utf-8') as f:    #打开文件
        data = f.read()   #读取文件
    x=re.split('PT P',data)[0]
    lis=[]
    for j in re.split('PT P',data):
        if j !=x:
            lis.append(j)
    #将所有的专利数据切割为单个的专利，并存在lis中
    print(file)
    for index in range(len(lis)):
        print(index,"####",file)
        result = re.split('\nPN |\nAB |\nPD |\nUT |\nER', lis[index])  # 固定长度为8
        PD = result[-3]
        PD_list=PD.split('\n')
        #print(PD)
        #print(PD_list)
        patent=PD_list[0].split("   ")[0].replace('-', '')
        for pd in PD_list:
            pa_num = pd.strip().split("   ")[0]
            pa_num = pa_num.replace('-', '')
            sql = "UPDATE `citations_2` SET cited = %s WHERE cited = %s"
            cur.execute(sql, (patent, pa_num))
            conn.commit()
            sql = "UPDATE `citations_2` SET citing = %s WHERE citing = %s"
            cur.execute(sql, (patent, pa_num))
            conn.commit()


