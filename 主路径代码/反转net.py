'''import pyecharts
from pyecharts import options as opts
from pyecharts.charts import Graph
path='C://Users//WSX//Desktop//total.txt'
with open(path, "r", encoding='utf-8') as f:  # 打开文件
    wenjian = f.read()
    text=wenjian.split("\n")
num=int(text[0].split(" ")[1])
patent=[]
for i in range(1,num+1):
    patent.append(text[i].split("\"")[1])
nodes = []
links = []
for i in patent:
    nodes.append({"name": i, "symbolSize": 10})
for i in range(num+2,len(text)-1):
    citing=int(text[i].strip().split()[0])
    cited=int(text[i].strip().split()[1].split()[0])
    links.append({"source": patent[citing-1], "target":  patent[cited-1]})
print(links)
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))
    .render("C://Users//WSX//Desktop//graph_base.html")
)




'''


'''from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
net=network()
g=nx.DiGraph()#创建空的有向图
path='C://Users//WSX//Desktop//total.txt'
with open(path, "r", encoding='utf-8') as f:  # 打开文件
    wenjian = f.read()
    text=wenjian.split("\n")
num=int(text[0].split(" ")[1])
patent=[]
for i in range(1,num+1):
    patent.append(text[i].split("\"")[1])
nodes = []
links = []
g.add_nodes_from(patent)
for i in range(num+2,len(text)-1):
    citing=int(text[i].strip().split()[0])
    cited=int(text[i].strip().split()[1].split()[0])
    g.add_edges_from([(patent[citing-1], patent[cited-1])])
nt.show("dot.html")
plt.show()
'''
import pymysql
path='E:\科研训练\主路经\\2022.txt'
with open(path, "r", encoding='utf-8') as f:  # 打开文件
    wenjian = f.read()
    text=wenjian.split("\n")
num=int(text[0].split(" ")[1])
patent=[]
shiyin=[]
beiyin=[]
patent.append(text[0])#包含说明后专利序列从1开始
for i in range(1,num+1):
    if text[i].split("\"")[1][0]=='#':
        patent.append(text[i].split("\"")[1].split("#")[1])
    else:
        patent.append(text[i].split("\"")[1])
for i in range(num+2,len(text)-1):
    citing=int(text[i].strip().split()[0])
    cited=int(text[i].strip().split()[1].split()[0])
    shiyin.append(patent[citing])
    beiyin.append(patent[cited])
print(shiyin[0])
print(beiyin[0])
conn = pymysql.connect(host='localhost', port=3306, charset='utf8', user='root', password='00long1216', db='patent_final')
cur = conn.cursor()
sql = 'truncate table spc_2022'
cur.execute(sql)
conn.commit()
for i in range(len(shiyin)):
    sql="insert into spc_2022 values (%s,%s)"
    cur.execute(sql,(beiyin[i],shiyin[i]))
    conn.commit()
cur.close()
conn.close()