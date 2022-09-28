import selenium.webdriver.support.expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




browser = webdriver.Chrome(executable_path='/Users/kristi/PycharmProjects/pythonProject/webdriver/chromedriver')


try:
    browser.get('https://stepik.org/catalog')
    vhod =  browser.find_element(By.CSS_SELECTOR,'[class*="auth_login"]').click()

    em=browser.find_element(By.ID,'id_login_email')
    em.send_keys('crzssssss')
    print('isdfjsdnfisdifnsdifnisdjfoisdfsdfsdfdsfsdfsdfsdfcvxcv')

    par=browser.find_element(By.ID,'id_login_password')
    par.send_keys('zzz')

    voiti = browser.find_element(By.CSS_SELECTOR,'[type=submit]').click()
    time.sleep(10)

    browser.get('https://stepik.org/lesson/236205/step/2?unit=208637')

    browser.execute_script('window.scrollBy(0, 300);')
    time.sleep(100)
    browser.switch_to.alert
    print('test222222')



finally:
    browser.close()
    browser.quit()
