from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp")
print(driver.title)

firstName = driver.find_element_by_name("firstName")
firstName.send_keys("Ramesh")

lastName = driver.find_element_by_name("lastName")
lastName.send_keys("Jaiswal")

email = driver.find_element_by_name("Username")
email.send_keys("RameshJ09876")

password = driver.find_element_by_name("Passwd")
password.send_keys("@Sandeep0987654")

confirm = driver.find_element_by_name("ConfirmPasswd")
confirm.send_keys("@Sandeep0987654")

firstName.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()

