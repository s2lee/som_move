import time

import pyautogui
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ID = "id"
PASSWORD = "password"

driver = uc.Chrome()
url = "https://somcloud.com/user/login"
driver.get(url)
driver.find_element(By.CSS_SELECTOR, ".g_id_signin").click()
driver.switch_to.window(driver.window_handles[1])

time.sleep(2)
pyautogui.write(ID)
pyautogui.press("enter")
time.sleep(3)
pyautogui.write(PASSWORD)
pyautogui.press("enter")
print(driver.window_handles[-1])

print(driver.page_source)
