import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get('https://lk.smarthome.rt.ru/')
time.sleep(5)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('GeckoDriver')

search_box.submit()

wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))

print(first_result.text)

driver.quit()


time.sleep(5)  # Let the user actually see something!
driver.quit()
