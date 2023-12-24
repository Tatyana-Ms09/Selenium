from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_url = "https://estro.ua/login"

phone = "987776655"
password = "your_password"

driver = webdriver.Chrome()

def test_login():
    try:
        driver.get(login_url)

        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "phone_number"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        phone_input.send_keys(phone)
        password_input.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Продовжити']"))
        )
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='welcome-message']"))
        )

        assert "Welcome" in driver.page_source

    finally:
        driver.quit()

test_login()
