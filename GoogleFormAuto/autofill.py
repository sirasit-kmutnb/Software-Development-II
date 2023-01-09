from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
# option.add_argument("--headless") Use this and the following option to run Headless
# option.add_argument("disable-gpu")
browser = webdriver.Chrome(
    executable_path='/chromedriver', options=option)

browser.get("https://forms.gle/eRRJdXUqBrPezvip6")

# Use the following snippets to get elements by their class names
textboxes = browser.find_elements(input, 'quantumWizTextinputPaperinputInput')

# textboxes = browser.find_elements_by_class_name(
#     "quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name(
    "docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name(
    "quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_class_name(
    "appsMaterialWizButtonPaperbuttonContent")

# Use the following snippets to get elements by their XPath
# otherboxes = browser.find_element_by_xpath("<Paste the XPath here>")


radiobuttons[0].click()
textboxes[1].send_keys("Hello World")

checkboxes[2].click()

submitbutton[0].click()
