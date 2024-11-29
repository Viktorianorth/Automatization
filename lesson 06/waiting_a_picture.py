from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Please wait until the images are loaded...")
    )
    print("Текст 'Please wait until the images are loaded...' обнаружен.")

    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )
    print("Текст изменился на 'Done!'")

    try:
        image = driver.find_element(By.CSS_SELECTOR, '#award')
        print("Изображение найдено:", image.get_attribute("src"))
    except Exception:
        print("Изображение с ID 'award' не найдено.")

finally:
    driver.quit()