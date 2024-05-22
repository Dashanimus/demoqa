from components.components import WebElement
from pages.base_page import BasePage


class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_heading = WebElement(driver, '#section1Heading')
        self.section_content_one = WebElement(driver, '#section1Content > p')
        self.section_content_two = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section_content_two_other = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section_content_three = WebElement(driver, '#section3Content > p')
