import re
import jieba
from PIL import Image
from jieba.analyse import *
from openpyxl import load_workbook
from wordcloud import WordCloud
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

# jieba.suggest_freq('n', False)
# jieba.suggest_freq('和', False)
# jieba.suggest_freq('的', False)
# jieba.suggest_freq('关键字', False)
# jieba.suggest_freq('者', False)
#读取excel文件工作表Sheet1
workbook = load_workbook(r'exp\exp2\share\职位.xlsx')
worksheet = workbook['Sheet1']
#将Sheet1中H列内容写入txt文件
data = []
f = open(r'exp\exp2\output\职位信息.txt', 'w')
for row in range(2, worksheet.max_row + 1):
    data.append(worksheet['H'+str(row)].value)
f.write(str(data))
f.close()

#去除html标签
f = open(r'exp\exp2\output\职位信息.txt', 'r').read()
g = re.sub('<.*?>', '', f)
g = re.sub('nbsp', '', g)
g = re.sub('  ', '', g)
#清洗后数据写入新的txt
h = open(r'exp\exp2\output\职位信息-清洗后.txt', 'w')
h.write(g)
h.close()

#生成词云
#读取txt
f = open(r'exp\exp2\output\职位信息-清洗后.txt', 'r', encoding='GBK').read()
#分词
sep_list = jieba.lcut(f)
print('分词', type(sep_list), len(sep_list), sep_list)
#过滤停用词
# stopwords为停用词list，stop.txt停用词一行一个
stopwords = [line.strip() for line in open(r'exp\exp2\share\stop.txt', 'r', encoding='utf-8').readlines()]
print('停用词', type(stopwords), stopwords)
outstr = ''
for word in sep_list:
    if word not in stopwords:
        outstr += word
print('过滤停用词后', type(outstr), outstr)
#过滤后重新分词
outstr = jieba.lcut(outstr)
outstr = ' '.join(outstr)
print('再次分词后', type(outstr), outstr)
#生成词云图
#设置词云使用的字体
font = r'C:\Windows\Fonts\simsun.ttc'
wc = WordCloud(font_path=font, width=2400, height=1200, max_words=100)
ar15 = np.array(Image.open(r'exp\exp4\ar15.png'))
ar15_colors = wordcloud.ImageColorGenerator(ar15)
wc.generate(outstr)

fig, axes = plt.subplot(1, 3)


wc.to_file(r'exp\exp2\output\词云.jpg')
plt.figure(dpi=100)
plt.imshow(wc, interpolation='catrom')
plt.axis('off')
plt.show()
plt.close()

#生成词频
for keyword, weight in extract_tags(outstr, topK=50, withWeight=True, allowPOS=()):
    print('%s %s' % (keyword, weight))
