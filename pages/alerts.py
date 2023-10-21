from components.components import WebElement
from pages.base_page import BasePage


class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.alert_btn = WebElement(driver, '#alertButton')
        self.confirm_btn = WebElement(driver, '#confirmButton')
        self.conf_result = WebElement(driver, '#confirmResult')
        self.prompt_btn = WebElement(driver, '#promtButton')
        self.prompt_form_check = WebElement(driver, '#promptResult')

        self.btn_timer_alert = WebElement(driver, '#timerAlertButton')
