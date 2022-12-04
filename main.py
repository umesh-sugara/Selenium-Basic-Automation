from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

url = "https://www.linkedin.com/jobs/search/?currentJobId=3367210414&geoId=102713980&keywords=data%20analyst&location=India&refresh=true"

chrome_driver_path = url


driver = webdriver.Chrome(chrome_driver_path)
driver.get(chrome_driver_path)
time.sleep(3)


def signin():
    mailid="explorersera@gmail.com"
    password = "Umesh@1234"

    signin= driver.find_element(By.LINK_TEXT, "Sign in")
    signin.click()

    username = driver.find_element(By.CSS_SELECTOR, "#username ")
    username.send_keys(mailid)
    code = driver.find_element(By.CSS_SELECTOR, "#password ")
    code.send_keys(password)

    signbtn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    signbtn.click()

# def jobSearch():
#     search = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember24"]')
#     search.send_keys(Keys.ENTER)

def expfilter():
    expbtn = driver.find_element(By.XPATH , '//*[@id="ember131"]/button')
    expbtn.click()
    internship = driver.find_element(By.XPATH, '//*[@id="artdeco-hoverable-artdeco-gen-43"]/div[1]/div/form/fieldset/div[1]/ul/li[1]/label/p/span[1]')
    internship.click()

    entrylevel = driver.find_element(By.XPATH , '//*[@id="artdeco-hoverable-artdeco-gen-43"]/div[1]/div/form/fieldset/div[1]/ul/li[2]/label/p/span[1]')
    entrylevel.click()

    expFilter = driver.find_element(By.XPATH, '//*[@id="ember381"]/span')
    expFilter.click()


def easyapply():
    easy= driver.find_element(By.XPATH, '//*[@id="ember996"]')
    easy.click()

# def applyjob():
#     apply = driver.find_element(By.XPATH, '//*[@id="ember1150"]/span')
#     apply.click()


signin()
expfilter()
# easyapply()
# applyjob()


# count = driver.find_element(By.ID, "money")

# while int(count.text) < 10000:
#     temp.click()

while 3<4:
    time.sleep(2)

