from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)
