import time

from execnet.gateway_base import serve
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

class Test_Auto:
    def test_auto(self, driver):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://demowebshop.tricentis.com/login")
        driver.maximize_window()

        time.sleep(2)
        regester = driver.find_element(By.XPATH, "//input[@value='Register']")
        regester.click()
        time.sleep(2)

        gender = driver.find_element(By.XPATH, "//input[@id='gender-male']").click()

        firstname = driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("jay")
        lastname = driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Pandey")
        email = driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("asgfdff@asd.akesdjf")

        password = driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("123456")
        confirmpass = driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("123456")
        time.sleep(1)
        reg= driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        laptop = driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]")
        #driver.execute_script("arguments[0].scrollIntoView();", laptop)
        time.sleep(2)
        laptop.click()
        time.sleep(2)
        cart = driver.find_element(By.XPATH, "//span[normalize-space()='Shopping cart']")
        cart.click()
        tandc = driver.find_element(By.XPATH, "//input[@id='termsofservice']").click()
        time.sleep(2)
        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        time.sleep(2)

        country = driver.find_element(By.XPATH,"//select[@id='BillingNewAddress_CountryId']")
        Select(country).select_by_visible_text("India")
        city = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_City']").send_keys("asdf")
        address1 = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address1']").send_keys("asdf")
        pincode = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']").send_keys("123456")
        phone = driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']").send_keys("1234567890")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@onclick='Shipping.save()']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@class='button-1 payment-method-next-step-button']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@class='button-1 payment-info-next-step-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@value='Confirm']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input[value='Continue']").click()


        time.sleep(4)

        driver.close()









