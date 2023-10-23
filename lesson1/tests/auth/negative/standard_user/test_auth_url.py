from selenium import webdriver
from selenium import By
import time

driver = webdriver.Chrome()

def test_login_form():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    url_before = driver.current_url == "https://www.saucedemo.com/inventor.html"

    time.sleep(3)
    url_after = driver.current_url == "https://www.saucedemo.com/inventory.html"

    assert url_before != url_after

    driver.quit()