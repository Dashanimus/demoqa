from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_find_icon():  # Длинный вариант с выведением да - нет
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    icon = driver.find_element(By.CSS_SELECTOR, '#root > div > div.login_logo')

    if icon is None:
        print("No element")
    else:
        print("Yes")


def test_find_username():
    driver = webdriver.Chrome()
    driver.get("http://saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, '#user-name')
    except NoSuchElementException:
        assert False
    assert True


def test_find_password():
    driver = webdriver.Chrome()
    driver.get("http://saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, '#password')
    except NoSuchElementException:
        assert False
    assert True
