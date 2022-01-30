import selenium.webdriver as selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os,threading,time

user='x0gd0157@corphq.hk.pccw.com'
pwd='corphq-P@ssw0rd202109'
teams_link='https://teams.microsoft.com/'
ms_login_link='https://login.microsoftonline.com/'

# class Info_value_null_error(Exception):
#     print('Attendence Info should not be null')
# class alart_is_not_click_error(Exception):
#     print('alart is not click')

def init():
    os.system("C:\\Users\\micke\\PycharmProjects\\auto_attender\\chromedriver.exe")

def attendence_info():
    trigger_time =['1:00','3:00','5:00','7:00','9:00','21:00','23:00']
    real_time=time.strftime('%H:%M')
    for i in trigger_time:
        if real_time >= i:
            return f'{i} {time.strftime("%d/%m")} Savio'
        else:
            pass

def main():
    try:
        driver = selenium.Chrome()
        driver.get(ms_login_link)
    except Exception as e:
        threading.Thread(target=init).start()

    #ms login page
    loop =True
    while loop == True:
        try:
            email_input_action = driver.find_element(By.XPATH,'//input[@type="email"]')
            submit_button_action = driver.find_element(By.XPATH,'//input[@id="idSIButton9"]')
        except Exception as e:
            pass
        else:
            email_input_action.send_keys(user)
            submit_button_action.click()
            break

    #HKT login page
    loop = True
    while loop == True:
        try:
            pwd_input_action = driver.find_element(By.XPATH,'//input[@id="passwordInput"]')
            submit_button_action = driver.find_element(By.XPATH,'//span[@id="submitButton"]')

        except Exception as e:
            pass
        else:
            pwd_input_action.send_keys(pwd)
            submit_button_action.click()
            loop = False

    #stay sign page
    loop = True
    while loop == True:
        try:
            submit_button_action = driver.find_element(By.XPATH,'//input[@id="idBtn_Back"]')
        except Exception as e:
            pass
        else:
            submit_button_action.click()
            driver.get(teams_link)
            loop = False

    #ms Teams page HandOver tab

    loop = True
    while loop == True:
        try:
            tab_action = driver.find_element(By.XPATH,'//a[@aria-label="Handover. Press Enter to select or press Shift+F10 for more options"]')
        except Exception as e:
            pass
        else:
            tab_action.click()
            loop = False

    # ms teams page Attendence tab
    loop = True
    while loop==True:
        try:
            driver.switch_to.frame(
                frame_reference=driver.find_element(
                    By.XPATH,'//iframe[@title="Tasks by Planner and To Do Tab View"]'))
            driver.switch_to.frame(
                frame_reference=driver.find_element(
                    By.XPATH, '//iframe[@title="Planner Tab View"]'))
            tab_action = driver.find_element(By.XPATH,'//div[@aria-label="Add task card in Attendence column"]')

        except Exception as e:
            print(e)
        else:
            tab_action.click()
            loop = False
        finally:
            time.sleep(5)

    # ms teams attendence card
    loop = True
    while loop == True:
        try:
            info_input = driver.find_element(By.XPATH,'//input[@type="text"]')
            #submit_button_action = driver.find_element(By.XPATH,'//button[@class="addTaskButton"]')
            driver.execute_script('alert("Create new Attdence?")')

            # if EC.alert_is_present()(driver):
            #     raise Exception
            # if attendence_info() == None:
            #     raise Exception

        except Exception as e:
            print(e)
            #pass
        else:
            info_input.send_keys(attendence_info())
            #submit_button_action.click()

main()
