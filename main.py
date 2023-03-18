import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
url = "https://somcloud.com/user/login"
browser.get(url)

browser.find_element(By.CSS_SELECTOR, ".g_id_signin").click()
time.sleep(5)

browser.switch_to.window(browser.window_handles[1])
time.sleep(5)

elem = browser.find_element(By.CSS_SELECTOR, "#identifierId").send_keys("id")
# browser.find_element(By.CSS_SELECTOR, ".VfPpkd-RLmnJb").click()
