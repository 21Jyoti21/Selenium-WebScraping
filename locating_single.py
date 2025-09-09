from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=3C5P82EHCC7AR&sprefix=lap%2Caps%2C518&ref=nb_sb_noss_2")

elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
time.sleep(3)
# print(elem.text)
print(elem.get_attribute("outerHTML"))


time.sleep(4)
driver.close()