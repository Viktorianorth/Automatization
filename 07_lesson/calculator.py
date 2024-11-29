import pytest
from selenium import webdriver
from calculatorpage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay("45")

    for button in ['7', '+', '8', '=']:
        page.click_button(button)

    result_text = page.get_result_text()
    assert result_text == "15", f"Ожидался результат 15, но получен: {result_text}"