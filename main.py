
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
