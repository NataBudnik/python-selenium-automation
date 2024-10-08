from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
sleep(5)


driver.find_element(By.XPATH,"//*[@id='headerPrimary']/a[4]/span").click()
sleep(5)

driver.find_element(By.XPATH,"//*[@id='listaccountNav-signIn']/a/span").click()
sleep(5)



driver.quit()
