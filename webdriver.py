import time  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
URL = r"https://ek.ua/"
language ='[data-lang="ua"]'
input_selector = '[id="ek-search"]'
search_request = 'Macbook'
search_result = "b.hst"

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get(URL)
driver.minimize_window()
language_change = driver.find_element_by_css_selector(language)
language_change.click()
time.sleep(3)

input_block = driver.find_element_by_css_selector(input_selector)
input_block.send_keys(search_request)
input_block.send_keys(Keys.RETURN)
time.sleep(5)

actual_text = driver.find_element_by_css_selector(search_result).text
driver.implicitly_wait(15)
assert actual_text == search_request
print("Done")
time.sleep(5)

driver.close()