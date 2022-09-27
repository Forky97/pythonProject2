from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome(executable_path='/Users/kristi/PycharmProjects/pythonProject/webdriver/chromedriver')


try:

    def calc(c):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser.get('http://suninjuly.github.io/get_attribute.html')
    searchnumb = browser.find_element(By.CSS_SELECTOR,"img")
    x = searchnumb.get_attribute("valuex")
    number = calc(x)
    time.sleep(2)

    put=browser.find_element(By.CSS_SELECTOR,'#answer')
    put.send_keys(number)

    robot = browser.find_element(By.CSS_SELECTOR,'#robotCheckbox').click()
    rule = browser.find_element(By.CSS_SELECTOR,'#robotsRule').click()
    time.sleep(3)
    press = browser.find_element(By.CSS_SELECTOR,'button.btn').click()
    time.sleep(3)



finally:
    browser.close()
    browser.quit()