from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import pyautogui

index_number = 10

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Chrome()

browser.get('https://forms.gle/mC1ySFn63mZeiAeH8')
time.sleep(5)

text1 = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
text1.send_keys("Test")

for _ in range(index_number):
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

time.sleep(2)

checkbox = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]')
checkbox.click()


radio = browser.find_element(By.XPATH, '//*[@id="i12"]')
radio.click()

checkbox = browser.find_element(By.XPATH, '//*[@id="i26"]')
checkbox.click()
checkbox = browser.find_element(By.XPATH, '//*[@id="i29"]')
checkbox.click()
