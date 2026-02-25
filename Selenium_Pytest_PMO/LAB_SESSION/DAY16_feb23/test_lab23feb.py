import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# ==============================
# STANDARD VARIABLES
# ==============================

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


# ==============================
# FIXTURE - DRIVER SETUP
# ==============================

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(BASE_URL)
    yield driver
    driver.quit()


# ==============================
# TEST CASE
# ==============================

def test_complete_swaglabs_flow(driver):

    wait = WebDriverWait(driver, 10)

    try:
        # Login
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        time.sleep(4)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(4)
        # Verify Login Success
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

        # Add Product to Cart
        wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

        # Open Cart
        time.sleep(4)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(4)
        # Click Checkout
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # Verify Checkout Page
        assert "checkout-step-one" in driver.current_url

        print(" Test Passed Successfully")

    except TimeoutException as e:
        pytest.fail(f"Element Not Found or Timeout: {e}")

    except Exception as e:
        pytest.fail(f"Test Failed Due To: {e}")