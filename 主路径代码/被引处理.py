import multiprocessing
import os
import re
import time

import pymysql
from selenium import webdriver
'''def search(num_1,num_2):
    conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_new')
    cur = conn.cursor()
    driver = webdriver.Edge('E:\python\Scripts\msedgedriver.exe')
    path="E:\科研训练\被引\\1.txt"
    txts=[]
    with open(path, "r",encoding='utf-8') as f:    #打开文件
        data = f.read()   #读取文件
    x=re.split('PT P',data)[0]
    lis=[]
    for j in re.split('PT P',data):
        if j !=x:
            lis.append(j)
    #将所有的专利数据切割为单个的专利，并存在lis中
    for index in range(num_1,num_2):
        result = re.split('\nPN |\nAB |\nPD |\nCP|\nUT |\nER', lis[index])#固定长度为8
        PD=result[-4]
        CP=result[-3]
        pa_list=CP.split('\n')#存储被引的专利
        PD_list=PD.split("\n")#种子文献号
        patent=PD_list[0].split(" ")[0].replace('-', '')#种子文献号
        patent_list=[]
        print("#############################", patent, index)
        for pat in PD_list:
            patent_list.append(pat.strip().split(" ")[0])#存储种子文献的所有专利号
        for pa in pa_list:
            pat = pa.strip().split(' ')[0]
            print(index,pat)
            if (pat[0:2] == 'US' or pat[0:2] == 'WO') and pat not in patent_list:
                try:
                    pa_num = pat.replace('-', '')
                    url = "https://worldwide.espacenet.com/searchResults?submitted=true&locale=cn_EP&DB=EPODOC&ST=advanced&TI=&AB=&PN=" + \
                          pa_num.split('-')[0] + "&AP=&PR=&PD=&PA=&IN=&CPC=&IC="  # 初始搜索页面
                    driver.get(url)
                    time.sleep(2)
                    time_xpath = "//*[@id=\"contentRow_1\"]/td[6]"
                    text = driver.find_element_by_xpath(time_xpath).text
                    pa_time = text.split('\n')[2]
                    print(pa_num, pa_time)
                except:
                    if int(pa_num[2:6])<=2022:
                        pa_time=pa_num[2:6]
                        print("提取", pa_num)
                    else:
                        try:
                            url_1="https://worldwide.espacenet.com/patent/search/family/022143783/publication/US6353889B1?q="+pa_num.split('-')[0]
                            driver.get(url_1)
                            time.sleep(10)
                            time_xpath_1="//*[@id=\"biblio-publication-number-content\"]"
                            text = driver.find_element_by_xpath(time_xpath_1).text
                            pa_time=text.split('·')[1]
                            print("补充", pa_num)
                        except:
                            print("错误", pa_num)
                            continue
                sql = "insert into  patent_cited (Publication,Publication_date) values (%s,%s)"
                cur.execute(sql, (pa_num, pa_time))
                conn.commit()
                sql = "insert into citations_cited values (%s,%s)"
                cur.execute(sql, (pa_num, patent))
                conn.commit()
        time.sleep(20)
    cur.close()
    conn.close()'''


def search(num_1,num_2):
    conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_final')
    cur = conn.cursor()
    patent_group=[]
    sql="SELECT Publication FROM `patent_total`"
    cur.execute(sql)
    results = cur.fetchall()
    for res in results:
       patent_group.append(res[0]) ##存储所有需要的专利的所有专利号
    path = "E:\科研训练\cite"
    files = os.listdir(path)
    for i in range(num_1,num_2):  # 遍历文件夹
        position = path + '\\' + files[i]  # 构造绝对路径，"\\"，其中一个'\'为转义符
        print(position)
        with open(position, "r", encoding='utf-8') as f:  # 打开文件
            data = f.read()  # 读取文件
        x=re.split('PT P',data)[0]
        lis=[]
        for j in re.split('PT P',data):
            if j !=x:
                lis.append(j)
        #将所有的专利数据切割为单个的专利，并存在lis中
        print(i,"###############",files[i])
        for index in range(len(lis)):
            result = re.split('\nPN |\nTI |\nAB |\nPD |\nCP|\nUT |\nER', lis[index])#固定长度为8
            PN=result[1]
            CP=result[-3]
            pa_list=CP.split('\n')#存储被引的专利
            patent=PN.split(';')[0].strip().replace('-', '')
            print("#############################", patent, index)
            for pa in pa_list:
                pat = pa.strip().split(' ')[0]
                pa_num = pat.replace('-', '')
                if pa_num in patent_group:
                    print(pa_num,index)
                    sql = "insert into citations_1 values (%s,%s)"
                    cur.execute(sql, (pa_num, patent))
                    conn.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    one = multiprocessing.Process(target=search, args=(0, 11))  #
    two = multiprocessing.Process(target=search, args=(11, 22))  #
    three = multiprocessing.Process(target=search, args=(22, 34))
    one.start()
    three.start()
    two.start()
    one.join()
    two.join()
    three.join()