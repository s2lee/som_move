import time

import pyautogui
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ID = "id"
PASSWORD = "pw"

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
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])

with open("temp.html", "w", encoding="utf8") as f:
    f.write(driver.page_source)

array = []
for i in range(1):
    driver.find_element(By.XPATH, f'//*[@id="snb_middle"]/div[{i + 1}]/div/div').click()
    time.sleep(1)
    fold_count = driver.find_element(
        By.XPATH, f'//*[@id="snb_middle"]/div[{i + 1}]/div/div/span[2]'
    )
    for j in range(int(fold_count.text)):
        driver.find_element(
            By.XPATH, f'//*[@id="snb_middle"]/div[{i + 1}]/div/ul/li[{j + 1}]'
        ).click()
        time.sleep(1)
        date = driver.find_element(
            By.XPATH, f'//*[@id="container"]/div[2]/div[1]/div[1]/div[1]/span[2]'
        )
        content = driver.find_element(By.XPATH, '//*[@id="editor"]')

        array.append([i + 1, date.text, content.text])
        time.sleep(1)
    print(array)


# //*[@id="snb_middle"]/div[1]/div/div/span[2]
# //*[@id="snb_middle"]/div[2]/div[1]/div/div/span[2]
# //*[@id="snb_middle"]/div[2]/div[2]/div/div/span[2]
# //*[@id="snb_middle"]/div[2]/div[3]/div/div/span[2]
# elem = driver.find_element(By.XPATH, '//*[@id="snb_middle"]/div[1]/div/div')
# elem.click()

# elem = driver.find_element(By.XPATH, '//*[@id="snb_middle"]/div[1]/div/ul/li[1]')
# elem.click()
# time.sleep(2)
# array = []
# fold_count = driver.find_element(
#     By.XPATH, '//*[@id="snb_middle"]/div[1]/div/div/span[2]'
# )
# print(fold_count.text)

# date = driver.find_element(
#     By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[1]/div[1]/span[2]'
# )
# print(date.text)

# content = driver.find_element(By.XPATH, '//*[@id="editor"]')
# print(content.text)
while True:
    pass


# print(driver.page_source)
