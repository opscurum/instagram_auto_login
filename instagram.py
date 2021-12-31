from selenium import webdriver
import time
from selenium.webdriver.common.by import By



driver=webdriver.Firefox()
time.sleep(2)

driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(2)


driver.find_element(By.XPATH,("/html/body/div[1]/section/main/div/div/div[2]/p/a")).click()

time.sleep(4)

username=driver.find_element(By.NAME, ("username"))
password=driver.find_element(By.NAME, ("password"))

username.send_keys("umitaslanofficiall")
password.send_keys("")

driver.find_element(By.XPATH,("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]")).click()

time.sleep(2)