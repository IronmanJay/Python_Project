import requests
from lxml import etree
#列表用来保存所有的线路信息
items = []
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
def parse_navigation():
    url = 'https://zhengzhou.8684.cn/'
    r = requests.get(url,headers=headers)
    #解析内容，获取所有的导航链接
    tree = etree.HTML(r.text)
    #查找以数字开头的所有链接
    number_href_list = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
    #查找以字母开头的所有链接
    char_href_list = tree.xpath('//div[@class="bus_kt_r2"]/a/@href')
    #将需要爬取的所有链接返回
    return number_href_list + char_href_list
def parse_erji_route(content):
    tree = etree.HTML(content)
    #写xpath，获取每一个线路
    route_list = tree.xpath('//div[@id="con_site_1"]/a/@href')
    route_name = tree.xpath('//div[@id="con_site_1"]/a/text()')
    i = 0
    #遍历上面这个列表
    for route in route_list:
        print('开始爬取%s线路' % route_name[i])
        route =  'https://zhengzhou.8684.cn' + route
        #发送请求
        r = requests.get(url=route,headers=headers)
        #解析内容，获取每一路公交的详细url
        parse_sanji_route(r.text)
        print('结束爬取%s线路' % route_name[i])
        i += 1
def parse_sanji_route(content):
    tree = etree.HTML(content)
    #获取公交线路信息
    bus_number = tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]
    #获取运行时间
    run_time = tree.xpath('//p[@class="bus_i_t4"][1]/text()')[0]
    #获取票价信息
    ticket_info = tree.xpath('//p[@class="bus_i_t4"][2]/text()')[0]
    #获取公交公司
    bus_gongsi = tree.xpath('//p[@class="bus_i_t4"][3]/text()')[0]
    #获取更新时间
    gxsj = tree.xpath('//p[@class="bus_i_t4"][4]/text()')[0]
    #获取上行总站数
    total_list = tree.xpath('//span[@class="bus_line_no"]/text()')
    up_total = total_list[0]
    # #将里面的空格替换为空
    # up_total = up_total.repalce('\xa0','')
    #获取上行所有站名
    up_site_list = tree.xpath('//dic[@class="bus_line_site "][1]/div/div/a/text()')
    #获取异常，给一个空
    try:
        #获取下行总站数
        down_total = total_list[1]
        # # 将里面的空格替换为空
        # down_total = down_total.repalce('\xa0', '')
        #获取下行所有站名
        down_site_list = tree.xpath('//dic[@class="bus_line_site "][2]/div/div/a/text()')
    except Exception as e:
        down_total = ''
        down_site_list = []
    #将每一条公交的线路信息存放到字典中
    item = {
        '线路名' : bus_number,
        '运行时间' : run_time,
        '票价信息' : ticket_info,
        '更新时间' : gxsj,
        '上行站数' : up_total,
        '上行站点' : up_site_list,
        '下行站数' : down_total,
        '下行站点' : down_site_list,
    }
    items.append(item)
def parse_erji(navi_list):
    #遍历上面的列表，依次发送请求，解析内容，获取每一个页面所有的公交路线url
    for first_url in navi_list:
        first_url = 'https://zhengzhou.8684.cn' + first_url
        print('开始爬取%s所有的公交信息' % first_url)
        #发送请求
        r = requests.get(url=first_url,headers=headers)
        #解析内容，获取每一路公交的详细url
        parse_erji_route(r.text)
        print('结束爬取%s所有的公交信息' % first_url)
def main():
    #爬取第一页所有的导航链接
    navi_list = parse_navigation()
    #爬取二级页面，需要找到以1开头的所有公交路线
    parse_erji(navi_list)
    #爬取完毕
    fp = open('郑州公交.txt','w',encoding='utf8')
    for item in items:
        fp.write(str(item) + '\n')
    fp.close()
if __name__ == '__main__':
    main()