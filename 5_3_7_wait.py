from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
#隐式等待 begin
driver = webdriver.Chrome()
driver.get('https://www.itcast.cn/')
driver.implicitly_wait(10)
driver.switch_to.frame('chatIframe')
element = driver.find_element(By.CLASS_NAME,'service')
print(element.text)
#隐式等待 end
'''

#显式等待 begin
from selenium.webdriver.support.ui import WebDriverWait
driver_kxy = webdriver.Chrome()
driver_kxy.get('https://www.itcast.cn/')
driver_kxy.switch_to.frame('chatIframe')
element = WebDriverWait(driver_kxy, 10).until(
    lambda x:x.find_element(By.CLASS_NAME, 'service')
)
print(element.text)