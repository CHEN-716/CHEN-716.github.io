from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
element_kxy = driver.find_element(By.LINK_TEXT, '新闻').click()
print(element_kxy)
print(f'当前窗口：{driver.current_window_handle}')
time.sleep(10)
print(f'所有窗口：{driver.window_handles}')
driver.switch_to.window(driver.window_handles[0])
time.sleep(10)

