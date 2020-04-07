import pandas as pd
import csv
from multiprocessing import Pool
import time

def getdata(url):
    tb = pd.read_html(url)[0]  # 经观察发现所需表格是网页中第4个表格，故为[3]
    tb.to_csv(r'D:\stock.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
    time.sleep(0.5)
    print('第'+str(i)+'页抓取完成')

# 引入进程池
def myprocesspool(num=10):
    pool = Pool(num)
    results = pool.map(getdata, urls)
    pool.close()
    pool.join()
    return results

if __name__ == '__main__':
    urls = []
    # for i in range(1, 179):  # 爬取全部178页数据
    #     tmp = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
    #     urls.append(tmp)
    temp = 'https://www.worldometers.info/coronavirus/#countries'
    urls.append(temp)
    # 预先输入好表格的列名
    with open(r'D:\stock.csv', 'w', encoding='utf-8-sig', newline='') as f:
        csv.writer(f).writerow(['Country,Other', 'Totalases', '3', '4', '5', '6','7', '8',])
    myprocesspool(10)
