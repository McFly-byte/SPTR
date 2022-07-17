import re
import xlwt
import os


workbook = xlwt.Workbook(encoding='utf8')
# 创建一个worksheet
worksheet = workbook.add_sheet('zhuanli')  # 取名为y Worksheet
worksheet.write(0, 0, "序号")  #
worksheet.write(0, 1, "专利号")
worksheet.write(0, 2, "专利标题")
worksheet.write(0, 3, "摘要")
worksheet.write(0, 4, "IPC分类号")
worksheet.write(0, 5, "时间")
worksheet.write(0, 6, "UT")
#创建要用的excel表格，并定义表头

path="D:\desktop\科研训练\数据\人脸识别"
files=os.listdir(path)
txts=[]
for file in files: #遍历文件夹
    position = path+'\\'+ file #构造绝对路径，"\\"，其中一个'\'为转义符
    print(position)
    with open(position, "r",encoding='utf-8') as f:    #打开文件
        data = f.read()   #读取文件
        txts.append(data)
#遍历专利数据的文件夹，将所有的专利数据存在txts中
x=re.split('PT P',txts[0])[0]
print(x)
lis=[]
for i in txts:
    for j in re.split('PT P',i):
        if j !=x:
            lis.append(j)
            print(j)
print("专利数")
print(len(lis))
#将所有的专利数据切割为单个的专利，并存在lis中

for index in range(0,len(lis)):
    result = re.split('\nPN |\nTI |\nAB |\nIP |\nPD |\nUT |\nER', lis[index])#固定长度为8
    index = index+1
    worksheet.write(index, 0, index)
    for i in range(1,len(result)-1):
        worksheet.write(index, i, result[i])


workbook.save('./31000.xls')