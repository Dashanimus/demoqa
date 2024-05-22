from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        # объекты элементов
        self.text_elements = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(1) > span > div > div.header-text')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        self.elements = WebElement(driver, 'div:nth-child(1) > div > ul > li')
        self.element_mobile = WebElement(driver, 'div > nav')

        self.footer_text = WebElement(driver, '#app > footer > span')
        self.icon_center_element = WebElement(driver, 'div.col-12.mt-4.col-md-6')

        self.block_menu = WebElement(driver, 'div.row > div:nth-child(1)')
