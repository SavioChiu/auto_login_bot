import time

import selenium.webdriver as selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,threading,requests
from bs4 import BeautifulSoup

user='x0gd0157@corphq.hk.pccw.com'
pwd='corphq-P@ssw0rd202109'
link2='https://zh-hk.facebook.com/'
link='https://login.microsoftonline.com/'

def init():
    os.system("C:\\Users\\micke\\PycharmProjects\\auto_attender\\chromedriver.exe")

#threading.Thread(target=init).start()


driver = selenium.Chrome()
driver.get(link)

#ms login page
loop = True
while loop == True:
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "i0116"))
        )
        loop=False

    except Exception:
        pass

driver.find_element(By.ID,'i0116').send_keys(user)
driver.find_element(By.ID,'idSIButton9').click()

time.sleep(10)

#HKT login page
loop = True
while loop == True:
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "passwordInput"))
        )
        loop=False

    except Exception:
        pass

driver.find_element(By.ID,'passwordInput').send_keys(pwd)
driver.find_element(By.ID,'submitButton').click()

#ms Teams page
loop = True
while loop == True:
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(('ng-bind', "mh.decodeDisplayName(tab.displayName)"))
        )
        loop=False

    except Exception:
        pass

driver.find_element('ng-bind', "mh.decodeDisplayName(tab.displayName)").click()
