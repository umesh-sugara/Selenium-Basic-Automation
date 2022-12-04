from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'https://www.appbrewery.co/p/newsletter'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(chrome_driver_path)


# path='https://en.wikipedia.org/wiki/Main_Page'

# temp= driver.find_element(By.XPATH , '//*[@id="articlecount"]/a[1]')

temp = driver.find_element(By.NAME, 'email')
# print(temp.text)
temp.send_keys("Python@gmail.com")

btn = driver.find_element(By.NAME, 'commit')
btn.send_keys(Keys.ENTER)
