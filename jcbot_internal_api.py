import builtins

import traceback
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type',0)

driver = webdriver.Firefox(profile)
driver.get("https://web.whatsapp.com/")

input("Scan QR Code if required before proceeding")

wait = WebDriverWait(driver,10)
xpath_contact = "//*[@id='pane-side']/div/div/div/div[contains(.//*,'The Meme Garbage Can')]"
xpath_file = "//*[@class='_3z3lc']/li[1]/button/input"
driver.find_element_by_xpath(xpath_contact).click()


def jcbot_sendMessage(message):
    print("[INFO] BOT SEND")
    WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CLASS_NAME,"_3u328")))
    textbox = driver.find_element_by_class_name("_3u328")
    textbox.send_keys(message + '\n')
    #textbox.click()
    #driver.execute_script("document.getElementsByClassName('_3u328')[0].innerHTML = '"+message+"';")

def jcbot_sendFile(filename):
    print("[INFO] BOT SEND FILE")
    fb = driver.find_element_by_xpath("//div[@title='Attach']")
    fb.click()
    file_button = driver.find_element_by_xpath(xpath_file)
    file_path = '/home/skrypton/Pictures/' + filename
    file_button.send_keys(file_path)
    
    button_xp = "//*[@class='_1g8sv NOJWi']"
    WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH,button_xp)))
    
    driver.find_element_by_xpath(button_xp).click()
    

    
    
    
builtins.jcbot_sendMessage = jcbot_sendMessage
builtins.jcbot_sendFile = jcbot_sendFile
