from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import random
import time

# Loading environment variables
load_dotenv(".env")
TWITTER_ID = os.getenv("TW_Username")
TWITTER_PASSWORD = os.getenv("TW_Password")

# Setting up our web driver
chrome_driver_path = r"C:\Development\chromedriver.exe"
my_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=my_service)
driver.maximize_window()

# We need to sleep random times occasionally, because we don't want to be banned on Twitter

# Testing our Internet Speed
driver.get("https://www.speedtest.net/")
time.sleep(random.uniform(3, 4))

test = driver.find_element(By.CLASS_NAME, "start-text")
test.click()
time.sleep(random.uniform(42, 43))

# This is our Internet Speed test results
download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text

# Now going to twitter and post our results
driver.get("https://twitter.com/i/flow/login")
time.sleep(random.uniform(2, 3))

# Sign in with our credentials
form1 = driver.find_element(By.NAME, "text")
form1.send_keys(TWITTER_ID)

btn2 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div'
                                     '/div[2]/div[2]/div/div/div/div[6]/div')
btn2.click()
time.sleep(random.uniform(2, 3))

form2 = driver.find_element(By.NAME, "password")
form2.send_keys(TWITTER_PASSWORD)
btn3 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                     'div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
btn3.click()
time.sleep(random.uniform(3, 4))

# Tweet about our Internet Speed test results
btn4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
btn4.click()
time.sleep(random.uniform(3, 4))


form4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                      'div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div'
                                      '[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

form4.send_keys(f"My latest speedtest results; down-speed:{download_speed} Mbps, up-speed:{upload_speed} Mbps")

btn5 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                     'div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/'
                                     'div/span/span')
btn5.click()

# Done & Finish
time.sleep(random.uniform(3, 4))
driver.quit()



