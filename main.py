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

time.sleep(3)
pyautogui.write(ID)
pyautogui.press("enter")
time.sleep(4)
pyautogui.write(PASSWORD)
pyautogui.press("enter")
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])

array = []
for i in range(15, 27):
    project_div_idx1 = f"div[{2 if i else 1}]"
    project_div_idx2 = f"div[{i}]/div" if i else ""
    driver.find_element(
        By.XPATH, f'//*[@id="snb_middle"]/{project_div_idx1}/{project_div_idx2}/div/div'
    ).click()
    # time.sleep(5)
    fold_count = driver.find_element(
        By.XPATH,
        f'//*[@id="snb_middle"]/{project_div_idx1}/{project_div_idx2}/div/span[2]',
    )
    project_name = driver.find_element(
        By.XPATH,
        f'//*[@id="snb_middle"]/{project_div_idx1}/{project_div_idx2}/div/span[1]',
    )
    for j in range(int(fold_count.text)):
        item_selected_idx = f"div[{i}]" if i else ""
        driver.find_element(
            By.XPATH,
            f'//*[@id="snb_middle"]/{project_div_idx1}/{item_selected_idx}/div/ul/li[{j + 1}]',
        ).click()
        # time.sleep(2)
        date = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[1]/div[1]/span[2]')
            )
        )
        content = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="editor"]'))
        )

        array.append([project_name.text, j + 1, date.text, content.text])

    # print(array)

with open("temp.txt", "w", encoding="utf8") as f:
    for x in range(len(array)):
        f.write(f"{array[x][0]} - {array[x][1]}\n{array[x][3]}\n")

while True:
    pass

# print(driver.page_source)
