from selenium import webdriver
from selenium.webdriver.support .ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('D:/python/SeleniumCrawer/下拉框.html')
element = driver.find_element(By.TAG_NAME, 'select')
select = Select(element)
print(select)

select.select_by_index(2)
time.sleep(5)

select.select_by_value('audi')
time.sleep(5)

select.select_by_visible_text('Volvo--')
time.sleep(5)