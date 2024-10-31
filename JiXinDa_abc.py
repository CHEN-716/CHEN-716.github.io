#pip install selenium -i https://pypi.doubanio.com/simple
#chromedriver下载地址：https://chromedriver.chromium.org/downloads
from selenium import webdriver
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class JiXinDa_abc:
    def __init__(self):#初始化函数
        self.url = 'http://jxd.itheima.net/#/login'
        self.driver = webdriver.Chrome()

    #定义登录操作
    def login_abc(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        # txtUserElement = self.driver.find_element(By.CLASS_NAME, 'el-input__inner')
        # print(txtUserElement)
        # txtUserElement.send_keys('adc')

        #找到登录按钮
        btnLoginElement = self.driver.find_element(By.CLASS_NAME, 'login-btn')
        btnLoginElement.click()
        print(btnLoginElement)
        #单击“体验项目”
        # self.driver.find_element(By.ID, 'button').click()
        time.sleep(5)
        #定位短信服务菜单，使用[]查找元素中指定的属性名，contains包含指定的属性关键词，and表示与（两项属性同时具备)
        #li[2]，xpath中的路径序号是从1开始，不是从0开始算，这个跟语言中有所不同
        #'/html/body/div[1]/div/div[1]/ul/li[2]/div/div/span'
        sms_service_element_abc = self.driver.find_element(By.XPATH, '//div[contains(@class, "sider-bar") and contains(@class, "scole-bar")]/ul/li[2]/div/div/span')
        webdriver.ActionChains(self.driver).move_to_element(sms_service_element_abc).click(sms_service_element_abc).perform()

        #日志服务菜单
        service_log_abc = self.driver.find_element(By.XPATH,
                                                   '//div[contains(@class, "sider-bar") and contains(@class, "scole-bar")]/ul/li[2]/ul/li/ul/li[5]')
        webdriver.ActionChains(self.driver).move_to_element(service_log_abc).click(service_log_abc).perform()

        #到元素上方，右键-->检查-->定位到元素-->右键-->复制xpath
        inputXpath_abc = '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div/div[3]/div[1]/form/div/div[1]/div/div/div/input'
        #WebDriverWait等待元素完整加载，否则找不到元素会报错
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, inputXpath_abc))
        )

        self.driver.find_element(By.XPATH, inputXpath_abc).send_keys('闲云旅游')

        inputXpath_abc = '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div/div[3]/div[1]/form/div/div[4]/div/div/div/input'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, inputXpath_abc))
        )

        self.driver.find_element(By.XPATH, inputXpath_abc).send_keys('小兔仙')

        #搜索按钮
        inputXpath_abc = '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div/div[3]/div[1]/form/div/div[5]/div/div/div/button[1]'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, inputXpath_abc))
        )
        self.driver.find_element(By.XPATH, inputXpath_abc).click()

        #time.sleep(10)

    def get_data_abc(self):
        #提取网页表格数据
        title_list_abc = []
        #表头数据
        for i in range(1,9):
            #主意单斜杠与双斜杠的区别
            title = self.driver.find_element(By.XPATH,
                f'//div[@class="ReceiveLog"]/div[2]//thead//th[{i}]').text
            title_list_abc.append(title)
        print(title_list_abc)
        #表格内容
        content_info_abc= []
        # rowsNum = self.driver.find_elements(By.XPATH,
        #         f'//*[@id="app"]/div/div[2]/div[1]/div/div/div/div/div[3]/div[2]/div[1]/div[3]/table/tbody/tr')
        rowsNum = self.driver.find_elements(By.XPATH,
                f'//div[@class="ReceiveLog"]//table[@class="el-table__body"]/tbody/tr')
        print(f'len:{len(rowsNum)}')
        for i in range(1, len(rowsNum) + 1):
            content_abc = self.driver.find_element(By.XPATH,
                f'//div[@class="ReceiveLog"]//table[@class="el-table__body"]/tbody/tr[{i}]').text
            content_info_abc.append(dict(zip(title_list_abc, content_abc.splitlines())))

        print(content_info_abc)
        return content_info_abc

    def save_data_abc(self, data):
        try:
            with open('result.json', mode='a+', encoding='utf-8') as file:
                file.write(json.dumps(data, ensure_ascii=False))
        except Exception as e:
            print(e)

    def run_abc(self):
        self.login_abc()
        # result_abc = self.get_data()
        num = 1
        while True:
            time.sleep(2)
            # button = self.driver.find_element(By.XPATH, '//div[@class="ReceiveLog"]//div/button[@class="btn-next"]')
            button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div/div[3]/div[2]/div[2]/button[2]')
            if button.is_enabled():
                data_abc = self.get_data_abc()
                self.save_data_abc(data_abc)
                print(f'正在处理第{num}页的数据')
                num += 1
                button.click()
            else:
                last_data_abc = self.get_data_abc()
                print(f'正在处理第{num}页的数据')
                self.save_data_abc(last_data_abc)
                self.driver.close()
                print('done')
                break

if __name__ == '__main__':
    jxd_abc = JiXinDa_abc()
    jxd_abc.run_abc()