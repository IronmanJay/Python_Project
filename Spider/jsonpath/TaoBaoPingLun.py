import urllib.request
import urllib.parse
import json
import re
import jsonpath
'''
接口：
https://rate.taobao.com/feedRateList.htm?auctionNumId=559141739630&userNumId=100340983&currentPageNum=1&pageSize=20
'''
items_list = []
def main():
    #循环爬取多页内容
    url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId=597295057718&userNumId=395522079&currentPageNum=2&pageSize=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    request = urllib.request.Request(url=url,headers=headers)
    json_text = urllib.request.urlopen(request).read().decode()
    #去掉json格式字符串两边的非法字符
    json_text = json_text.strip('() \n\t\r')
    #将json格式字符串转化为python对象
    obj = json.loads(json_text)
    #抓取评论内容
    #用户头像、用户名、评论内容、评论时间、手机类型
    #首先取出comments这个列表
    comments_list = obj['comments']
    #遍历这个列表，循环取出每个评论
    for comment in comments_list:
        #用户头像
        user = jsonpath.jsonpath(comment,'$..user')
        face = 'http:' + user['avater']
        #用户名
        name = user['nick']
        #评论内容
        ping_content = comment['content']
        #评论时间
        ping_time = comment['date']
        #手机信息
        info = jsonpath.jsonpath(comment,'$..sku')[0]
        #将评论信息保存到字典中
        item = {
            '用户头像' : face,
            '用户名' : name,
            '评论' : ping_content,
            '事件' : ping_time,
            '信息' : info,
        }
        items_list.append(item)
if __name__ == '__main__':
    main()
    string = json.dumps(items_list,ensure_ascii=False)
    #保存到文件中
    with open('ping.txt','w',encoding='utf8') as fp:
        fp.write(string)