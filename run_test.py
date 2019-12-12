from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("督查督办")#定位到输入框，输入selenium2
driver.find_element_by_id("su").click()#定位到点击按钮，点击
h1 = driver.find_element_by_xpath("//div[@id='content_left']/div/div/h3/a")
time.sleep(3)
h1.click()
time.sleep(3)
driver.quit()