from selenium import webdriver
import time
#模拟创建一个浏览器对象，然后通过对象去操作浏览器
path = r'D:\Video\Python视频教程\第五阶段、爬虫开发\1、Python爬虫从入门到精通\Python爬虫-学习资料\day03\ziliao\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(3)
#查找input输入框
my_input = browser.find_element_by_id('kw')
#往框里面写文字
my_input.send_keys('风景')
time.sleep(3)
#查找搜索按钮
button = browser.find_elements_by_class_name('s_btn')[0]
button.click()
time.sleep(3)
#找到指定图片点击
image = browser.find_elements_by_class_name('op-img-address-link-imgs')[2]
image.click()
time.sleep(3)
#关闭浏览器,退出浏览器
browser.quit()