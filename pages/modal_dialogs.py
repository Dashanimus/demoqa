from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_all = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')

        # ДЗ 12
        self.count_elements_alerts = WebElement(driver, 'div > div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a')

        # Элементы small-modal
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.body_small_modal = WebElement(driver, 'div.modal-body')
        self.title_small_modal = WebElement(driver, '#example-modal-sizes-title-sm')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')

        # Элементы large-modal
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.title_large_modal = WebElement(driver, '#example-modal-sizes-title-lg')
        self.body_large_modal = WebElement(driver, 'div.modal-body > p')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal')
        self.list_btn = WebElement(driver, '#modalWrapper > div > button')
