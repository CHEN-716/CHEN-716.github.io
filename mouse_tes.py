from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
'''
#鼠标单击 begin
driver.get('https://www.baidu.com/')
driver.maximize_window()
element = driver.find_element(By.ID, 's-top-loginbtn')
ActionChains(driver).click(on_element=element).perform()
#鼠标单击 end
time.sleep(5)
#鼠标悬停 begin

driver.get('https://www.itcast.cn/')
element = driver.find_element(By.CLASS_NAME, 'a_gd')
print(element.text)
ActionChains(driver).move_to_element(element).perform()

#鼠标悬停 end
'''

driver.get('https://portal.fuyunfeng.top/plugins_v2/index.html#/slider-verify-example')
element = driver.find_element(By.XPATH, "//div[@id='circle']")
#创建鼠标移动对象
action = ActionChains(driver)
#按住鼠标左键
action.click_and_hold(element)
#向右拖拽XX像素
action.drag_and_drop_by_offset(element, 100, 0)
time.sleep(2)
action.perform()

time.sleep(20)