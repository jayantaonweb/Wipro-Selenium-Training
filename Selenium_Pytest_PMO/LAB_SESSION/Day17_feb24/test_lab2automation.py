import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager


class TestAutomationPractice:
    def test_page(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        # ------------------ Radio Button ------------------
        driver.find_element(By.XPATH, "//input[@value='radio2']").click()
        time.sleep(1)

        # ---------------- Suggestion Class ----------------
        # Enter partial country name
        driver.find_element(By.ID, "autocomplete").send_keys("Ind")
        time.sleep(2)

        # Capture all suggestions
        countries = driver.find_elements(By.CSS_SELECTOR, "li.ui-menu-item div")

        # Loop and select "India"
        for country in countries:
            if country.text == "India":
                country.click()
                break

        print("Selected country successfully!")

        time.sleep(2)

        # ------------------ Checkbox ------------------
        driver.find_element(By.ID, "checkBoxOption1").click()
        time.sleep(1)

        # ------------------ Dropdown ------------------
        dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
        dropdown.select_by_visible_text("Option2")
        time.sleep(1)

        # ------------------ Alert ------------------
        driver.find_element(By.ID, "name").send_keys("Jayanta")
        driver.find_element(By.ID, "alertbtn").click()

        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()
        time.sleep(1)

        # ------------------ Switch Window ------------------
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        print("New Window Title:", driver.title)
        driver.close()

        driver.switch_to.window(windows[0])
        time.sleep(1)

        # -------- Switch to iframe --------
        driver.switch_to.frame("courses-iframe")

        # -------- Get all text inside iframe --------
        all_text = driver.find_element(By.TAG_NAME, "body").text

        print("----- IFRAME TEXT START -----")
        print(all_text)
        print("----- IFRAME TEXT END -----")

        # Switch back to main page
        driver.switch_to.default_content()

        time.sleep(2)

        driver.quit()
