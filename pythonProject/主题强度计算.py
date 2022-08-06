import pymysql
import pandas as pd
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import MWETokenizer
from nltk.corpus import stopwords
import re
# TODO 处理完LDA和困惑度曲线再来看

def duqu1(year):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Xy213592', db='patent')
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT(*) FROM `专利31000` WHERE `时间` >= '" + str(year)+"' AND `时间` <= '" + str(year+1)+"'")  # 多少条记录
        #cur.execute("SELECT * FROM `专利7000`  ")  # 多少条记录
        data = cur.fetchall()
        frame = pd.DataFrame(list(data),columns=['jishu'])
    except:
        frame = pd.DataFrame()
    return frame
    conn.commit()
    cur.close()
    conn.close()

def shuzi():
    shuzilist = [0]
    a = 0
    for i in range(2000,2022,2):
        print(i)
        juzhen1 = duqu1(i)
        juzhen2 = list(juzhen1['jishu'])
        a += juzhen2[0]
        shuzilist.append(a)
    return shuzilist

shuzilist = shuzi()
print(shuzilist)

def duqu():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Xy213592', db='patent_for_test')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM `专利31000_for_test` WHERE `时间` >= 2000 AND `时间` <= 2021 ORDER BY `时间`  ")  # 多少条记录
        data = cur.fetchall()
        frame = pd.DataFrame(list(data), columns=['patent', 'ab', 'ipc', 'time'])
    except:
        frame = pd.DataFrame()
    return frame
    conn.commit()
    cur.close()
    conn.close()

# 获取单词的词性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def englishfenci(mytext):
    # 引入分词表中引入词组
    cizu = []
    biaozhun = []
    f = open("C:/Users/mcfly/Desktop/主题模型代码文件/必备文件/6（分词典）.txt", "r")
    lines = f.readlines()  # 读取全部内容
    for line in lines:
        line = line.strip('\n')
        line = line.lower()
        biaozhun.append(line)
    biaozhun = list(set(biaozhun))
    for i in biaozhun:
        k = i.split(" ")
        cizu.append(tuple(k))
    tokenizer = MWETokenizer(cizu, separator='_')

    # 还原词性
    m = re.sub(r'[0-9]+', '', mytext)
    a = re.sub(':|!|,|/|”|;|’|`', ' ', m)
    y = a.replace('(', '')
    x = y.replace(')', '')
    p = x.replace('.', ' ')
    print(p)
    tokens = tokenizer.tokenize(word_tokenize(p))  # 分词
    words = []
    word_list = []
    tagged_sent = pos_tag(tokens)  # 获取单词词性
    wnl = WordNetLemmatizer()
    for t in tagged_sent:
        wordnet_pos = get_wordnet_pos(t[1]) or wordnet.NOUN
        word_list.append(wnl.lemmatize(t[0], pos=wordnet_pos))  # 词形还原
    stopWords = set(stopwords.words('english'))
    for w in word_list:
        a = w.lower()
        if a not in stopWords:
            words.append(w)
    return (" ").join(words)

data = duqu()
data["content_cutted"] = data.ab.apply(englishfenci)

def print_top_words(model, feature_names, n_top_words):
    tword = []
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        topic_w = ";".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        tword.append(topic_w)
        print(topic_w)
    return tword

# 把数据转换成lda所需要的数据
#n_features = 5000  # 提取1000个特征词语
tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                #max_features=n_features,
                                stop_words=set(stopwords.words('english')),
                                max_df=0.5,
                                min_df=10)
tf = tf_vectorizer.fit_transform(data.content_cutted)

# 定义主题的数量
n_topics = 27
lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                learning_method='batch',
                                learning_offset=150,
                                doc_topic_prior=0.5,  # 参数阿尔法
                                topic_word_prior=0.1,  # 参数贝塔
                                random_state=0)
docres = lda.fit_transform(tf)#文档-主题矩阵

def qiangdu(juzhen,num1,num2):
    zqd = []
    for i in range(27):
        sum = float('0')
        for m in range(num1,num2):
            num = juzhen[m][i]
            sum += num
        qd = sum/(num2-num1)
        zqd.append(qd)
    return zqd

def zjz(juzhen):
    shuzilist = shuzi()
    print(shuzilist)
    zqd = []
    for i in range(11):
        linshi = qiangdu(juzhen,shuzilist[i],shuzilist[i+1])
        zqd.append(linshi)
    return zqd

zqd = zjz(docres)
print(zqd)

# ### 作图

from pylab import *
def plot(zqd):
    nianfen = []
    for i in range(0,22,2):
        a = i+2000
        nianfen.append(a)
    list1 = [0,1,4,6,7,14,18,19,20,21,22,25,26]
    list2 = [2,5,11,12,13,16,17]
    list3 = [3,8,9,10,15,23,24]
    markers = ['o', 's', '^', 'p', '.', 'v',
               ',', 'd', 'h', '2', 'x',
               '4', 'd', '+', 'v', 'x']
    plt.clf()
    plt.figure(figsize=(24, 10))
    plt.xticks(nianfen, rotation=45)
    for i,b in zip(list1,markers):
        linshi = []
        for m in zqd:
            linshi.append(m[i])
        plt.plot(nianfen, linshi, marker=b,markersize=6,label='topic_' + str(i + 1))
    plt.legend(loc="best")
    plt.xlabel('year')
    plt.ylabel('Intensity of theme')
    plt.savefig('图/人脸识别/强度图/曲折.png')

    plt.clf()
    plt.figure(figsize=(24, 10))
    plt.xticks(nianfen, rotation=45)
    for i,b in zip(list2,markers):
        linshi = []
        for m in zqd:
            linshi.append(m[i])
        plt.plot(nianfen, linshi, marker=b,markersize=6, label='topic_' + str(i + 1))
    plt.legend(loc="best")
    plt.xlabel('year')
    plt.ylabel('Intensity of theme')
    plt.savefig('/图/人脸识别/强度图/下降.png')

    plt.clf()
    plt.figure(figsize=(24, 10))
    plt.xticks(nianfen, rotation=45)
    for i,b in zip(list3,markers):
        linshi = []
        for m in zqd:
            linshi.append(m[i])
        plt.plot(nianfen, linshi, marker=b,markersize=6, label='topic_' + str(i + 1))
    plt.legend(loc="best")
    plt.xlabel('year')
    plt.ylabel('Intensity of theme')
    plt.savefig('图/人脸识别/强度图/上升.png')

    '''for i in range(27):
        linshi = []
        for m in zqd:
            linshi.append(m[i])
        plt.clf()
        plt.figure(figsize=(24, 16))
        plt.xticks(nianfen, rotation=45)
        plt.plot(nianfen, linshi, marker='o', markersize=6, label='topic_' + str(i + 1))
        plt.legend(loc="best")
        plt.xlabel('year')
        plt.ylabel('Intensity of theme')
        plt.savefig('D:\desktop\图\人脸识别\强度图/主题'+str(i+1)+'.png')'''
plot(zqd)


