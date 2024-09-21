from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()
options.add_argument("user-agent='nav-link-accountList-nav-line-1'")

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

driver.find_element(By.XPATH,"//*[@id='createAccountSubmit']").click()


driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.XPATH, "//*[@id='ap_email']")
driver.find_element(By.XPATH, "//*[@id='ap_password']")
driver.find_element(By.XPATH, "//*[@id='ap_password_check']")
driver.find_element(By.XPATH, "//*[@id='continue']").click()

sleep(10)

driver.quit()