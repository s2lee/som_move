import time

import pyautogui
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
    project_idx = 2 if i else 1
    project_div_idx = f"div[{i}]/div" if i else ""
    fold_count = driver.find_element(
        By.XPATH,
        f'//*[@id="snb_middle"]/div[{project_idx}]/{project_div_idx}/div/span[2]',
    )
    project_name = driver.find_element(
        By.XPATH,
        f'//*[@id="snb_middle"]/div[{project_idx}]/{project_div_idx}/div/span[1]',
    )
    for j in range(int(fold_count.text)):
        item_selected_idx = f"div[{i}]" if i else ""
        driver.find_element(
            By.XPATH,
            f'//*[@id="snb_middle"]/div[{i + 1}]/{item_selected_idx}/div/ul/li[{j + 1}]',
        ).click()
        time.sleep(1)
        date = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[1]/div[1]/span[2]')
            )
        )
        content = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="editor"]'))
        )

        array.append([project_name.text, j + 1, date.text, content.text])

    print(array)

while True:
    pass

# print(driver.page_source)
