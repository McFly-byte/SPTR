
import threading
import multiprocessing

def run(statement1,statement2):
    print( )
    print( statement1)
    print( statement2)

tm_begin=['', '2009', '2012', '2015', '2018', '2020']
tm_end=['2008', '2011', '2014', '2017', '2019', '2021']
tb, attr, n_topics_1, n_topics_2 = "专利", "时间",19,21
# TODO 多线程
count = len(tm_begin)
threads = []
for index in range(count-1):
    statement1, statement2 = "",""
    if str.isdigit(tm_begin[index]) == False:
        y2 = int( tm_end[index] )
        y3 = int( tm_begin[index+1] )
        y4 = int( tm_end[index+1] )
        statement1 = "SELECT * FROM `{0}` WHERE `{1}` <= {2}  ".format(tb,attr,y2)
        statement2 = "SELECT * FROM `{0}` WHERE `{1}` >= {2} AND `{1}` <= {3}".format(tb,attr,y3,y4)
    else :
        y1 = int(tm_end[index])
        y2 = int(tm_end[index])
        y3 = int(tm_begin[index + 1])
        y4 = int(tm_end[index + 1])
        statement1 = "SELECT * FROM `{0}` WHERE `{1}` >= {2} AND `{1}` <= {3}".format(tb, attr, y1, y2)
        statement2 = "SELECT * FROM `{0}` WHERE `{1}` >= {2} AND `{1}` <= {3}".format(tb, attr, y3, y4)
    # cos.cos_similarity(self.user, self.pwd, self.db, statement1,statement2)

    t = threading.Thread(target=run,args=(statement1,statement2))     # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    threads.append(t)

for t in threads:
    t.setDaemon(True)
    t.start()
    t.join()


