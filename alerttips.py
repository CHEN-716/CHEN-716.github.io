from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('D:/python/SeleniumCrawer/警告提示框.html')
#Alert begin
element = driver.find_element(By.ID, 'btnAlert').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.accept()  #点击确认按钮
#Alert end

time.sleep(3)

#Confirm begin
element = driver.find_element(By.ID, 'btnConfirm').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(2)
alert.accept()
#alert.dismiss()
#Confirm end
time.sleep(3)

#prompt begin
element = driver.find_element(By.ID, 'btnPrompt').click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(1)
alert.send_keys('张三')  #输入文本
time.sleep(2)
alert.accept()   #点击确定按钮
# prompt end
time.sleep(5)
