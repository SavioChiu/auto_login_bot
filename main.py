import selenium.webdriver as selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,threading,time

user='x0gd0157@corphq.hk.pccw.com'
pwd='corphq-P@ssw0rd202109'
teams_link='https://teams.microsoft.com/'
ms_login_link='https://login.microsoftonline.com/'

def init():
    os.system("C:\\Users\\micke\\PycharmProjects\\auto_attender\\chromedriver.exe")

#threading.Thread(target=init).start()


driver = selenium.Chrome()
driver.get(ms_login_link)

#ms login page
loop = True
while loop == True:
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "i0116"))
        )

        driver.find_element(By.ID, 'i0116').send_keys(user)
        driver.find_element(By.ID, 'idSIButton9').click()
        loop = False

    except Exception:
        pass

#HKT login page
loop = True
while loop == True:
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "passwordInput"))
        )

        driver.find_element(By.ID, 'passwordInput').send_keys(pwd)
        driver.find_element(By.ID, 'submitButton').click()
        loop = False

    except Exception:
        pass

#stay sign page (optional)
loop = True
while loop == True:
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, "idBtn_Back"))
        )
        driver.find_element(By.ID, 'idBtn_Back').click()
        driver.get(teams_link)
        loop = False

    except Exception:
        pass

#ms Teams page
loop = True
while loop == True:
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(('ng-bind', "mh.decodeDisplayName(tab.displayName)"))
        )
        driver.find_element('ng-bind', "mh.decodeDisplayName(tab.displayName)").click()
        loop=False

    except Exception:
        pass

