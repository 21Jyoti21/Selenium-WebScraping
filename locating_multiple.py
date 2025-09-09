from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
query="laptop"

#ek se lekar 20 page pe jitti queries hongi wo dega
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3C5P82EHCC7AR&sprefix=lap%2Caps%2C518&ref=nb_sb_noss_2")
    # https://www.amazon.in/s?k=laptop&page=2&xpid=onBn4dAx_SZ7h&crid=3C5P82EHCC7AR&qid=1757338940&sprefix=lap%2Caps%2C518&ref=sr_pg_2
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    # time.sleep(3)
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elem.text)
    # print(elem.text)


    time.sleep(4)
    driver.close()