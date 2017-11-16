# -*- coding: UTF-8 -*-

#统计谷歌浏览器访问历史记录

import os
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt

def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain =sublevel_split[0].replace("www.", "")
        return domain
    except IndexError:
        print('URL format error!')

def analyze(results):
    prompt =input("[.] Type <c> to print or <p> to plot\n[>] ")

    if prompt == "c":
        with open('./history.txt','w') as f:
            for site, count in sites_count_sorted.items():
                f.write(site+'\t'+str(count)+'\n')
    elif prompt == "p":
        key=[]
        value=[]
        for k,v in results.items():
            key.append(k)
            value.append(v)
        n=25
        X=range(n)
        Y=value[:n]
        plt.bar(X,Y,align='edge')
        plt.xticks(rotation=45)
        plt.xticks(X,key[:n])
        for x,y in zip(X,Y):
            plt.text(x+0.4, y+0.05,y, ha='center', va= 'bottom')
        plt.show()
    else:
        print("[.] Uh?")
        quit()

if __name__=='__main__':
    #path to user's history database (Chrome)
    data_path=r'D:\\'
    files=os.listdir(data_path)

    history_db = os.path.join(data_path, 'history')

    #querying the db
    c = sqlite3.connect(history_db)

    cursor = c.cursor()
    select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
    # select_statement = "SELECT * FROM downloads;"

    cursor.execute(select_statement)


    results = cursor.fetchall() #tuple

    sites_count = {} #dict makes iterations easier :D
    print(results)

    for url, count in results:
        url = parse(url)
        if url in sites_count:
            sites_count[url] += 1
        else:
            sites_count[url] = 1

    sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

    analyze (sites_count_sorted)
    cursor.close()