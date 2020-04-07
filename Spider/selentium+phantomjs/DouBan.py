from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.douban.com/")

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))


login_ele = driver.find_element_by_css_selector("li.account-tab-account").login_ele.click()

driver.find_element_by_id("username").send_keys("IronmanJay")

driver.find_element_by_id("password").send_keys("mimanibuzhidao741")

time.sleep(2)

driver.find_element_by_class_name("btn btn-account btn-active").click()

time.sleep(2)

cookies = {i["name"]:i["value"] for i in driver.get_cookie()}

print(cookies)

login_ele.quit()

