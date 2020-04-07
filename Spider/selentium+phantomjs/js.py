from selenium import webdriver
import time
#phantomjs路径
path = r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
#创建浏览器对象
browser = webdriver.PhantomJS(path)
url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv.html'
browser.get(url)
time.sleep(3)
with open(r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\phantomjs\tupian1.html','w',encoding='utf8') as fp:
    fp.write(browser.page_source)
js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)
with open(r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\phantomjs\tupian2.html','w',encoding='utf8') as fp:
    fp.write(browser.page_source)
browser.quit()