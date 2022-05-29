from selenium import webdriver
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = "D:/CODE/Hackathon/chromedriver.exe"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get("https://copy.ai") 

driver.find_element('sign-in-google').click()
#driver.find_element_by_id("sign-in-google").click()