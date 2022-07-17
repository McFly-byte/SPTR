import pymysql


def time(time1,time2):#创建保存时间窗数据的表格
    conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_final')
    cur = conn.cursor()
    if time1 == 0:
        sql = "CREATE table citations_%s(cited varchar(255),citing varchar(255)) "
        cur.execute(sql, time2)
    else:
        sql="CREATE table citations_%s_%s(cited varchar(255),citing varchar(255)) "
        cur.execute(sql,(time1,time2))
    cur.close()
    conn.close()
def spc(time1,time2):#创建保存spc的表格
    conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_final')
    cur = conn.cursor()
    if time1 == 0:
        sql = "CREATE table spc_%s(cited varchar(255),citing varchar(255)) "
        cur.execute(sql, time2)
    else:
        sql="""CREATE table spc_%s_%s(cited varchar(255),citing varchar(255))"""
        cur.execute(sql,(time1,time2))
    cur.close()
    conn.close()
def search1(lis):###提取施引或被引在时间窗内的引文关系
    conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_final')
    cur = conn.cursor()
    sql = 'truncate table citations_time'
    cur.execute(sql)
    conn.commit()
    num = int(len(lis) / 30000)  # 将全部专利切分成小份，防止sql语句过长
    results=[]
    for n in range(num + 1):
        if (n + 1) * 30000 <= len(lis):
            listt = [lis[i] for i in range(n * 30000, (n + 1) * 30000)]
        else:
            listt = [lis[i] for i in range(n * 30000, len(lis))]
        #print('\n\n\n')
        new_sql = "SELECT  distinct * FROM citations_true where citing in('" + listt[0]
        for pa in range(1, len(listt)):
            new_sql = new_sql + "','" + listt[pa]
        new_sql = new_sql + "')"
        #print((new_sql))##sql语句没有问题
        cur.execute(new_sql)
        result = cur.fetchall()
        for re in result:
            results.append(re)
    for re in results:
        sql="insert into citations_time values ('"+re[0]+"','"+re[1]+"')"
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
def search2(lis,time1,time2):###提取施引或被引在时间窗内的引文关系
    conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_final')
    cur = conn.cursor()
    num = int(len(lis) / 30000)  # 将全部专利切分成小份，防止sql语句过长
    results=[]
    for n in range(num + 1):
        if (n + 1) * 30000 <= len(lis):
            listt = [lis[i] for i in range(n * 30000, (n + 1) * 30000)]
        else:
            listt = [lis[i] for i in range(n * 30000, len(lis))]
        new_sql = "SELECT * FROM citations_time where cited in('" + listt[0]
        for pa in range(1, len(listt)):
            new_sql = new_sql + "','" + listt[pa]
        new_sql = new_sql + "')"
        #print(new_sql)##sql语句没有问题
        cur.execute(new_sql)
        result = cur.fetchall()
        for re in result:
            results.append(re)
    time(time1,time2)
    for re in results:
        if  time1==0:
            sql = "insert into citations_%s values ('" + re[0] + "','" + re[1] + "')"
            print(sql)
            cur.execute(sql,time2)
        else:
            sql="insert into citations_%s_%s values ('"+re[0]+"','"+re[1]+"')"
            print(sql)
            cur.execute(sql,(time1,time2))
        conn.commit()
    spc(time1, time2)
    cur.close()
    conn.close()
def total(time1,time2):
    conn = pymysql.connect(host='localhost', port=3306, charset='utf8',user='root', password='00long1216', db='patent_final')
    cur = conn.cursor()
    patent=[]
    sql = "SELECT Publication,Publication_date FROM `patent_total` WHERE Publication_date>= %s and Publication_date<=%s "##获取某个时间窗的专利号与时间
    cur.execute(sql,(time1,time2))
    res = cur.fetchall()
    for re in res:###将时间窗内的专利取出
        patent.append(re[0])
    patent=list(set(patent))
    search1(patent)
    search2(patent,time1,time2)
total(2019,2022)
