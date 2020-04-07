from selenium import webdriver
import time
#phantomjs路径
path = r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
#创建浏览器对象
browser = webdriver.PhantomJS(path)
url = 'https://movie.douban.com/typerank?type_name=爱情&type=13&interval_id=100:90&action='
browser.get(url)
time.sleep(3)
browser.save_screenshot(r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\phantomjs\douban.png')
#让browser执行简单的js代码，模拟滚动条滚动到底部
js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)
browser.save_screenshot(r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\phantomjs\douban2.png')
#获取网页的代码，保存到文件中
html = browser.page_source
with open(r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\phantomjs\douban.html','w',encoding='utf8') as fp:
    fp.write(html)
browser.quit()