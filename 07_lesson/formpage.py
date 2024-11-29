from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_field(self, field_name, value):
        field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, field_name))
        )
        field.clear()
        field.send_keys(value)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        submit_button.click()

    def get_field_color(self, field_id):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        return field.value_of_css_property('background-color')