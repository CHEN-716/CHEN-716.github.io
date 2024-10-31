from selenium import webdriver
import time

driver = webdriver.Chrome() #定义一个浏览器
driver.maximize_window() #最大化窗口
driver.get("http://www.baidu.com") #打开网址

driver.find_element_by_id('')
time.sleep(2)

driver.get("https://jd.com")
time.sleep(2)

driver.back()  #后退
time.sleep(2)
driver.forward() #前进
time.sleep(2)
driver.refresh()


print(driver.title)
driver.save_screenshot('jd.png') #保存网页截图

time.sleep(20)