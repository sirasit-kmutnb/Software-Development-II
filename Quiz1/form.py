from selenium import webdriver
from selenium.webdriver.common.by import By

#option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='/Volumes/SSDEx/chromedriver')

browser.get("https://forms.gle/xphJfdQf4rJN8gvc8")

textboxes = browser.find_elements('xpath',"/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
# radiobuttons = browser.find_element("docssharedWizToggleLabeledLabelWrapper")
# checkboxes = browser.find_element("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_elements(By.CLASS_NAME,"uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd")


if textboxes:
    # Send keys to the first textbox
    textboxes[0].send_keys("Test")
else:
    print("No textbox elements found")
    print(textboxes)


