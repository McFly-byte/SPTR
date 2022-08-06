import pymysql
from nltk.tokenize import MWETokenizer, word_tokenize
import pandas as pd
import re
from nltk.corpus import stopwords  # 停用词表
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt

# ### 1. 数据处理

def duqu1():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Xy213592', db='patent_for_test')
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM `专利31000_for_test` WHERE `时间` >= 2020 AND `时间` <= 2021 ")  #选定时间窗
        data = cur.fetchall()
        frame = pd.DataFrame(list(data),columns=['patent','ab','ipc','time'])
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
    f = open("C:/Users/mcfly/Desktop/主题模型代码文件/必备文件/6（分词典）.txt", "r") #这个文件是自己子自定义添加的分词典
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
    stopWords = set(stopwords.words('english')) #这是所选取的停用词表
    for w in word_list:
        a = w.lower()
        if a not in stopWords:
            words.append(w)
    return (" ").join(words)

data = duqu1()
data["content_cutted"] = data.ab.apply(englishfenci)

# ### 2.LDA分析

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
n_topics = 30  #这一步非常重要，是定义主题模型分析出来的主题数量，需要根据困惑度曲线来定义
lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                learning_method='batch',
                                learning_offset=150,
                                doc_topic_prior=0.5,  # 参数阿尔法
                                topic_word_prior=0.1,  # 参数贝塔
                                # 不写默认alpha和beta是1/主题数
                                random_state=0)
docres = lda.fit_transform(tf)#文档-主题矩阵
#print(docres)
#print(lda.components_)#主题-词矩阵


###########每个主题对应词语
n_top_words = 30
tf_feature_names = tf_vectorizer.get_feature_names()
topic_word = print_top_words(lda, tf_feature_names, n_top_words)
# TODO 主题词输出到软件中
df = pd.DataFrame()
df['topic'] = topic_word
df.to_excel("zhutici_2021.xlsx",index=False)#输出对应的主题和其主题词



# ### 3.画出困惑度曲线


plexs = []
n_max_topics =50
for i in range(1, n_max_topics):
    print(i)
    lda = LatentDirichletAllocation(n_components=i, max_iter=50,
                                    learning_method='batch',
                                    learning_offset=150, random_state=0)
    lda.fit(tf)
    plexs.append(lda.perplexity(tf))

n_t = 49  # 区间最右侧的值。注意：不能大于n_max_topics
x = list(range(1, n_t))
plt.figure(figsize=(24,8))
plt.plot(x, plexs[1:n_t])
plt.xlabel("number of topics")
plt.ylabel("perplexity")
plt.show()