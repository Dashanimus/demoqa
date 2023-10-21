from components.components import WebElement
from pages.base_page import BasePage


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        # Поля для заполнения пользователя
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.e_mail = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        # Кнопки
        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_clr = WebElement(driver, "span[title='Delete']")
        self.btn_add = WebElement(driver, '#addNewRecordButton')

        self.submit = WebElement(driver, '#submit')
        self.edit = WebElement(driver, '#edit-record-4 > svg > path')
        self.btn_delete = WebElement(driver, '#delete-record-4 > svg > path')
        self.num_str = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.str_five = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.previous = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.next = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')

        # Для webtables valid
        self.btn_delete_row = WebElement(driver, '[title="Delete"]')
        self.modal_dialog = WebElement(driver, "#registration-form-modal")
        self.table = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table")
        self.btn_edit_4 = WebElement(driver, '#edit-record-4 > svg > path')
        self.btn_delete_4 = WebElement(driver, '#delete-record-4 > svg > path')

        # Страницы
        self.current_page = WebElement(driver, "input[type=number]")
        self.total_page = WebElement(driver, "span.-pageInfo > span")

        # Для fill form
        self.inp_first = WebElement(driver, '#firstName')
        self.inp_last = WebElement(driver, '#lastName')
        self.inp_mail = WebElement(driver, '#userEmail')
        self.inp_age = WebElement(driver, '#age')
        self.inp_salary = WebElement(driver, '#salary')
        self.inp_department = WebElement(driver, '#department')

        # Для sort
        self.btn_columns = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div.rt-th.rt-resizable-header.-sort-asc.-cursor-pointer > div.rt-resizable-header-content')

    def fill_form(self,
                  inp_first='First',
                  inp_last='Last',
                  inp_mail='example@mail.com',
                  inp_age='23',
                  inp_salary='5000',
                  inp_department='Development'
                  ):
        self.inp_first.send_keys(inp_first)
        self.inp_last.send_keys(inp_last)
        self.inp_mail.send_keys(inp_mail)
        self.inp_age.send_keys(inp_age)
        self.inp_salary.send_keys(inp_salary)
        self.inp_department.send_keys(inp_department)
