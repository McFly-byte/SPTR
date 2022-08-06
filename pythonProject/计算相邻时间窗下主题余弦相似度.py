import math
from nltk.stem import WordNetLemmatizer
import pymysql
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np
import openpyxl
from nltk.tokenize import MWETokenizer, word_tokenize
import os
import pandas as pd
import re
from nltk.corpus import stopwords  # 停用词表
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
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
def duqu1():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Xy213592', db='patent')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM `专利31000` WHERE `时间` <= 2008  ")
        data = cur.fetchall()
        frame = pd.DataFrame(list(data),columns=['patent','ab','ipc','time'])
    except:
        frame = pd.DataFrame()
    return frame
    conn.commit()
    cur.close()
    conn.close()

def duqu(year1,year2):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Xy213592', db='patent')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM `专利31000` WHERE `时间` >= "+str(year1)+" AND `时间` <= " +str(year2))  # 多少条记录
        data = cur.fetchall()
        frame = pd.DataFrame(list(data),columns=['patent','ab','ipc','time'])
    except:
        frame = pd.DataFrame()
    return frame
    conn.commit()
    cur.close()
    conn.close()
# 将词组添加到字典中并分词
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

    #还原词性
    m = re.sub(r'[0-9]+', '', mytext)
    a = re.sub(':|!|,|/|”|;|’|`', ' ', m)
    y = a.replace('(','')
    x = y.replace(')','')
    p = x.replace('.',' ')
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





#分词处理
data1 = duqu1()
data2 = duqu(2009,2011)
data1["content_cutted"] = data1.ab.apply(englishfenci)
data2["content_cutted"] = data2.ab.apply(englishfenci)


# 得到两个时间窗下词袋中的所有单词
tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                #max_features=n_features,
                                stop_words=set(stopwords.words('english')),
                                max_df=0.5,
                                min_df=10)
tf1 = tf_vectorizer.fit_transform(data1.content_cutted)
tf_feature_names1 = tf_vectorizer.get_feature_names()

tf2 = tf_vectorizer.fit_transform(data2.content_cutted)
tf_feature_names2 = tf_vectorizer.get_feature_names()



# 得到两个时间窗下的主题-词矩阵
n_topics1 = 21
n_topics2 = 19
lda1 = LatentDirichletAllocation(n_components=n_topics1, max_iter=50,
                                learning_method='batch',
                                learning_offset=150,
                                doc_topic_prior=0.5,  # 参数阿尔法
                                topic_word_prior=0.1,  # 参数贝塔
                                random_state=0)
lda2 = LatentDirichletAllocation(n_components=n_topics2, max_iter=50,
                                learning_method='batch',
                                learning_offset=150,
                                doc_topic_prior=0.5,  # 参数阿尔法
                                topic_word_prior=0.1,  # 参数贝塔
                                random_state=0)
docres1 = lda1.fit_transform(tf1)#文档-主题矩阵
juzhen1 = lda1.components_
docres2 = lda2.fit_transform(tf2)
juzhen2 = lda2.components_

#取两个时间窗下词袋的并集
hengzhou = []
for i in tf_feature_names1:
    hengzhou.append(i)
for i in tf_feature_names2:
    if i not in tf_feature_names1:
        hengzhou.append(i)

#得到合并词袋后的主题-词矩阵
for m in range(len(juzhen1)):
    a = []
    for i in hengzhou:
        if i in tf_feature_names1:
            p = tf_feature_names1.index(i)
            a.append(juzhen1[m][p])
        else:
            a.append(float(0))
    if m == 0:
        combine1 = np.array(a)
    else:
        combine1 = np.vstack((combine1,a))


for m in range(len(juzhen2)):
    a = []
    for i in hengzhou:
        if i in tf_feature_names2:
            p = tf_feature_names2.index(i)
            a.append(juzhen2[m][p])
        else:
            a.append(float(0))
    if m == 0:
        combine2 = np.array(a)
    else:
        combine2 = np.vstack((combine2,a))

# 计算余弦相似度
def compute_cosine(vec1, vec2):
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vec1)):
        sum += vec1[i] * vec2[i]#两个向量的维度相同
        sq1 += pow(vec1[i], 2)
        sq2 += pow(vec2[i], 2)
    try:
        result = float(sum) / (math.sqrt(sq1) * math.sqrt(sq2))
    except ZeroDivisionError:
        result = 0.0
    # print(result)
    return result



#计算主题间的余弦相似度并输出
xsdjz = []
for i in combine1:
    hz = []
    for m in combine2:
        result = compute_cosine(i, m)
        hz.append(result)
    xsdjz.append(hz)
df = pd.DataFrame()
df['topic_相似度'] = xsdjz
df.to_excel("topic_cosine_lda_2008_2011.xlsx",index=False)
