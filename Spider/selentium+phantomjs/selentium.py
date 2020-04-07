from selenium import webdriver
import time

# driver = webdriver.Chrome()

driver = webdriver.PhantomJS()

# driver.set_window_size(1920,1080)

driver.maximize_window()

driver.get("http://www.baidu.com")

driver.save_screenshot("./baidu.png")

driver.find_element_by_id("kw").send_keys("python")

driver.find_element_by_id("su").click()

# cookies = driver.get_cookies()
#
# print(cookies)3
#
# print("*"*100)
#
# cookies = {i["name"]:i["value"] for i in cookies}
#
# print(cookies)

print(driver.page_source)

time.sleep(3)

driver.quit()