from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.user_number = WebElement(driver, '#userNumber')
        self.current_address = WebElement(driver, '#currentAddress')
        self.hobbies = WebElement(driver, '#hobbiesWrapper')

        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')

        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')

        self.user_form = WebElement(driver, '#userForm')
        self.state = WebElement(driver, '#state')
        self.city = WebElement(driver, '#city > div')
        self.inp_state = WebElement(driver, '#react-select-3-input')

        # ДЗ 9*
        self.btn_NCR = WebElement(driver, "//*[contains(text(), 'NCR')]", 'xpath')
        # self._state_form = WebElement(driver, '#state')
        # self.select_state = WebElement(driver, '#react-select-input')
        # self.select_cty = WebElement(driver, '#react-select-4-input')
        # self.city_form = WebElement(driver, '#city')
