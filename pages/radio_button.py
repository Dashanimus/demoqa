from components.components import WebElement
from pages.base_page import BasePage


class Radio(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, 'div:nth-child(2) > label')
        self.impressive = WebElement(driver, 'div:nth-child(2) > div:nth-child(3) > label')
        self.no = WebElement(driver, 'div:nth-child(2) > div.custom-control.disabled.custom-radio.custom-control-inline > label')

        self.text = WebElement(driver, 'p.mt-3')
