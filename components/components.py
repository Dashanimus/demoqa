# Отделяем методы работы с элементом от работы со страницей
# Здесь классы методов над кнопками, иконками и т.д.

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class WebElement:
    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)
        # Поиск элементов, когда надо посчитать кол-во эл-ов или сделать цикличную проверку

    def check_count_elements(self, count: int):
        if len(self.find_elements()) == count:
            return True
        return False

    def click(self):
        self.find_element().click()  # Метод клик по элементу

    def click_force(self):
        self.driver.execute_script("arguments[0].click()", self.find_element())
        # Всегда так пишем [0], используем в кранйем случае, если перекрывает кнопку

    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);",
            "window.scrollTo(0,document.body.scrollHeight);",
            self.find_element()
        )

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return self.find_element().text

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)
        if value is None:
            return False
        if len(value) > 0:
            return value
        return True  # Пустая строка, если нет атрибута

    def get_by_type(self):  # Метод для работы с любым типом локатора
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + " not correct")
            return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def visible(self):
        return self.find_element().is_displayed()

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)
