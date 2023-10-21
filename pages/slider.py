from components.components import WebElement
from pages.base_page import BasePage


class Slider(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.value = WebElement(driver, 'input#sliderValue.form-control')
        self.btn_slide = WebElement(driver, '#sliderContainer > div.col-9 > span > input')
