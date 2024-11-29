import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from internet_storepage import storePage


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    shop_page = storePage(driver)
    shop_page.open("https://www.saucedemo.com/")
    shop_page.login("standard_user", "secret_sauce")
    shop_page.add_items_to_cart()
    shop_page.go_to_cart()
    shop_page.checkout()
    shop_page.fill_checkout_form("Viktoria", "Mikhaylova", "123456")

    total_value = shop_page.get_total_price()

    assert total_value == "58.29", (
        f"Expected total to be $58.29, but got ${total_value}. "
        "Проверьте итоговую сумму в корзине."
    )