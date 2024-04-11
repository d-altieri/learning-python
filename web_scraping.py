from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://poedb.tw/us/Vendor_recipe_system")
page = driver.find_element(By.TAG_NAME, value="tr")
print(page.text)
driver.implicitly_wait(4.0)

driver.quit()