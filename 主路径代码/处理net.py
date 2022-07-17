import pymysql
def net(time1,time2):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='00long1216', db='patent_final')
    cur = conn.cursor()
    shiyin=[]#存储所有引文关系的施引
    beiyin=[]#存储所有引文关系的被引
    if time1==0:
        sql = 'select * from citations_%s'
        cur.execute(sql,  time2)
        result=cur.fetchall()
    else:
        sql='select * from citations_%s_%s'
        cur.execute(sql,(time1,time2))
        result = cur.fetchall()
    for users in result:
        shiyin.append(users[1])#存储所有的施引专利
        beiyin.append(users[0])#存储所有的被引专利
    patent=list(set(shiyin+beiyin))#所要使用的不重复的专利表
    conn.commit()
    cur.close()
    conn.close()
    dic={}
    print(len(patent))
    for i,pa in enumerate(patent):
        print(i,pa)
        dic[pa]=i+1
    if time1 == 0:
        path = "citations_"+ str(time2) + ".txt"
    else:
        path="citations_"+str(time1)+"_"+str(time2)+".txt"
    with open(path,"w") as f:
        f.write("*Vertices  ")
        f.write( str(len(patent)))
        f.write("\n")
        for i,pa in enumerate(patent):
            f.write("  ")
            f.write(str(i+1))
            f.write("  ")
            f.write(pa)
            f.write("\n")
        f.write("*Arcs  ")
        f.write( "\n")
        for i in range(len(shiyin)):
            f.write("  ")
            f.write(str(dic[shiyin[i]]))
            f.write(" ")
            f.write(str(dic[beiyin[i]]))
            f.write("\n")
if __name__ == '__main__':
    net(0,2022)