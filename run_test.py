from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)#设置隐式等待10秒
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("督查督办")#定位到输入框，输入selenium2
driver.find_element_by_id("su").click()#定位到点击按钮，点击
sreach_window = driver.current_window_handle
h2 = len(driver.find_elements_by_xpath("//div[@cmatchid='225']"))
h3 = 1
list = []
while h3 <= h2:
    num = int("300%d"%(h3))
    h1 = driver.find_element_by_xpath("//div[@id='300%d']/div/h3/a"%(h3))
    h1.click()
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != sreach_window:
            driver.switch_to.window(handle)
            driver.close()
    for handle in all_handles:
        if handle == sreach_window:
            driver.switch_to.window(handle)
    h3 = h3+1
sleep(3)
driver.quit()