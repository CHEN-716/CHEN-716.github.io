from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome() #定义一个浏览器
driver.get('http://news.baidu.com')

element = driver.find_element(By.CLASS_NAME, 'en')
print(element.text)

element = driver.find_element(By.TAG_NAME, 'a')
print(element)
