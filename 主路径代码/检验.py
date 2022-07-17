import time

import pymysql
from selenium import webdriver

'''conn = pymysql.connect(host='localhost', port=3306, user='root', password='00long1216', db='patent_true')
cur = conn.cursor()
sql = 'select * from spc_2022'
cur.execute(sql)
result = cur.fetchall()
shiyin = []  # 存储所有引文关系的施引
beiyin = []  # 存储所有引文关系的被引
driver = webdriver.Edge('E:\python\Scripts\msedgedriver.exe')
driver.implicitly_wait(10)
for users in result:
    shiyin.append(users[1])  # 存储所有的施引专利
    beiyin.append(users[0])  # 存储所有的被引专利
for i in range(len(shiyin)):
    sql="SELECT Publication,Publication_date FROM `patent_true` where Publication ='"+shiyin[i]+"'"
    cur.execute(sql)
    result1= cur.fetchall()
    print(shiyin[i])
    try:
        time1=result1[0][1]
    except:
        url = "https://worldwide.espacenet.com/searchResults?submitted=true&locale=cn_EP&DB=EPODOC&ST=advanced&TI=&AB=&PN="+shiyin[i].split('-')[0]+"&AP=&PR=&PD=&PA=&IN=&CPC=&IC="  # 初始搜索页面
        print(url)
        driver.get(url)
        time = "//*[@id=\"contentRow_1\"]/td[6]"
        text = driver.find_element_by_xpath(time).text
        time1=text.split('\n')[2]
    sql="SELECT Publication,Publication_date FROM `patent_true` where Publication ='"+beiyin[i]+"'"
    print(beiyin[i])
    cur.execute(sql)
    result2 = cur.fetchall()
    try:
        time2 = result2[0][1]
    except:
        url = "https://worldwide.espacenet.com/searchResults?submitted=true&locale=cn_EP&DB=EPODOC&ST=advanced&TI=&AB=&PN="+beiyin[i].split('-')[0]+"&AP=&PR=&PD=&PA=&IN=&CPC=&IC="  # 初始搜索页面
        print(url)
        driver.get(url)
        time = "//*[@id=\"contentRow_1\"]/td[6]"
        text = driver.find_element_by_xpath(time).text
        time2=text.split('\n')[2]
    print(shiyin[i], time1)
    print(beiyin[i], time2)
    if time1<time2:
        print("#################################出错")
        print(shiyin[i],time1)
        print(beiyin[i],time2)
        continue
'''
import pymysql
from selenium import webdriver

conn = pymysql.connect(host='localhost', port=3306, user='root', password='00long1216', db='patent_final')
cur = conn.cursor()
sql = 'select * from citations_2'
cur.execute(sql)
result = cur.fetchall()
shiyin = []  # 存储所有引文关系的施引
beiyin = []  # 存储所有引文关系的被引
for users in result:
    shiyin.append(users[1])  # 存储所有的施引专利
    beiyin.append(users[0])  # 存储所有的被引专利
for i in range(len(shiyin)):
    sql="SELECT Publication,Publication_date FROM `patent_total` where Publication ='"+shiyin[i]+"'"
    cur.execute(sql)

    result1= cur.fetchall()
    time1=result1[0][1]
    sql="SELECT Publication,Publication_date FROM `patent_total` where Publication ='"+beiyin[i]+"'"
    cur.execute(sql)

    result2 = cur.fetchall()
    time2 = result2[0][1]
    print(shiyin[i], time1)
    print(beiyin[i], time2)
    if time1<time2:
        print("#################################出错")
        sql = "DELETE FROM citations_2 where cited=%s and citing=%s"
        cur.execute(sql,(beiyin[i],shiyin[i]))
        conn.commit()
        continue

