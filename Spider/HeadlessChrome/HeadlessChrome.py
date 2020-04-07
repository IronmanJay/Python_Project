from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
#创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#驱动路径
path = r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\ziliao\chromedriver_win32\chromedriver.exe'
#创建浏览器对象
browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
#上网
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)
browser.save_screenshot(r'baidu.png')
browser.quit()