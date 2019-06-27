from selenium.webdriver.common.action_chains import ActionChains
import traceback
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from jcbot_internal_api import *
import modules
import time


#textbox.send_keys("[JCBOT] THIS IS A TEST MESSAGE\n")

print("Final: ",builtins.commands)
savedMessage = ""
while True:
    register=driver.find_elements_by_class_name("P6z4j")
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/span[2]/div/span[2]').click()
    except:
        pass
    if len(register) > 0:
        ele = register[-1]
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(ele, 0, -20)
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
    try:
        xpath_latest_message = "//*[@class='_1ays2']/div[last()]/div/div/div[contains('.//span','')]/div[@class='_12pGw EopGb']/span"
        xpath_info = "//*[@class='_1ays2']/div[last()]/div/div/div[contains(@class,'copyable-text')]"
        wait.until(EC.presence_of_element_located((By.XPATH,xpath_latest_message)))
        latestMessage = driver.find_element_by_xpath(xpath_latest_message).text
        userInfo = driver.find_element_by_xpath(xpath_info).get_attribute('data-pre-plain-text').split("]")
        if (latestMessage != savedMessage):
            savedMessage = latestMessage
            # Parse command
            if (savedMessage.startswith("jc!")):
                builtins.userList = (userInfo[0][1:], userInfo[1][1:-2])
                print("[LOG] Candidate Message: ",latestMessage, "Footprint: ",userList)
                builtins.argsList = savedMessage.split(' ')
                if (builtins.argsList[0][3:] in builtins.commands.keys()):
                    print("[LOG] Command: "+latestMessage[3:])
                    builtins.commands[builtins.argsList[0][3:]]()
    except Exception as ex:
        print("[WARN] Unable to retrieve Message, ")
        traceback.print_exc()
