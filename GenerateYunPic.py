from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import jieba
import numpy

# jieba.load_userdict('user_dict.txt')

from wordcloud import WordCloud
with open("wordlist.txt" ,encoding="utf-8")as wordlist:
    try:
        strings = wordlist.read()
    finally:
        wordlist.close()
    wordlist_af_jieba = jieba.cut_for_search(strings)
    wl_space_split = ' '.join(wordlist_af_jieba)
    stopwords=set(STOPWORDS)
    fstop=open('chineseStopWords_1.txt','r',encoding='UTF-8')
    for eachWord in fstop:
        stopwords.add(eachWord.encode('utf-8'))
    wc=WordCloud(font_path=r'C:\Windows\Fonts\simfang.ttf', background_color='black',max_words=200,width=700,height=1000,stopwords=stopwords,max_font_size=100,random_state=30)
    wc.generate(wl_space_split)
    wc.to_file('hupu_pubg2.png')
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')

