from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://lojaloja.pt/shop/p/kwjbwcntsnkneu1nz7i49ccw6k0p1o")

price_dollar = driver.find_element(By.CSS_SELECTOR, value=".product-price")
print(price_dollar.text)

# driver.close()
driver.quit()
