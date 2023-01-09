from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)

browser.get('https://forms.gle/mC1ySFn63mZeiAeH8')

text1 = browser.find_element(
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# text1.send_keys("Test")
