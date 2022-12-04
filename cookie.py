from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'http://orteil.dashnet.org/experiments/cookie/'
chrome_driver_path = url


driver = webdriver.Chrome(chrome_driver_path)
driver.get(chrome_driver_path)


temp = driver.find_element(By.ID, "cookie")
count = driver.find_element(By.ID, "money")

while int(count.text) < 10000:
    temp.click()
