from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import pyautogui
import os
from dotenv import load_dotenv

# create .env file and set EMAIL and PASSWORD of gmail

load_dotenv()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Chrome()

browser.get('https://forms.gle/7yZK12RhgKZZQUzA7')
time.sleep(5)

login_url = browser.find_element(
    By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[2]')
login_url.click()

time.sleep(2)

email = browser.find_element(By.XPATH, '//*[@id="identifierId"]')
email.send_keys(os.getenv('EMAIL'))

topassword = browser.find_element(
    By.XPATH, '//*[@id="identifierNext"]/div/button')
topassword.click()

time.sleep(2)

password = browser.find_element(
    By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(os.getenv('PASSWORD'))

login = browser.find_element(
    By.XPATH, '//*[@id="passwordNext"]/div/button')
login.click()

time.sleep(5)

text1 = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
text1.send_keys("Test")

dropdown = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div')
dropdown.click()
for _ in range(2):
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

time.sleep(2)

choice = browser.find_element(
    By.XPATH, '//*[@id="i9"]')
choice.click()

time.sleep(1)

# radio = browser.find_element(By.XPATH, '//*[@id="i9"]/div[3]')
# radio.click()

checkbox = browser.find_element(By.XPATH, '//*[@id="i23"]')
checkbox.click()
# checkbox1 = browser.find_element(By.XPATH, '//*[@id="i30"]')
# checkbox.click()

next_page = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
next_page.click()

time.sleep(5)

text_area = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
text_area.send_keys("Richmannnn!!!!!!!!!")

submit = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
submit.click()
