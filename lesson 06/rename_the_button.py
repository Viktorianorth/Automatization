from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.CSS_SELECTOR, "input#newButtonName")
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
    button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "button#updatingButton"), "SkyPro"))

    print(button.text)

finally:
    driver.quit()