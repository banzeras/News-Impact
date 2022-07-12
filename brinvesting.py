#!/usr/bin/python3

from selenium import webdriver 

from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://br.investing.com/equities/ambev-pn-news/78"

driver.get(url)

time.sleep(2)

#service.find_element(By.XPATH,"//*[@id='clickMe']").click()

