from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager import chrome
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=ChromeService(chrome.ChromeDriverManager().install))

driver.get("https://google.com")

time.sleep(5)

driver.close()
driver.quit()
