from components.components import WebElement
from pages.base_page import BasePage


class DemoQA(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1) > div > div.card-body')
        self.start_url = 'https://demoqa.com/'
        self.tools_qa = WebElement(driver, '#app > footer > span')
        self.center = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/text()')
        self.h5 = WebElement(driver, 'div.card-body > h5')

    # def exist_icon(self):
    #     try:
    #         self.icon.find_element() #поиск для конкретного элемента
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     return self.find_element(locator='#app > header > a').click()
    #
    # def click_on_the_btn_something(self):
    #     return self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()
