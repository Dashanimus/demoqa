from pages.elements_page import ElementsPage
from pages.check_box import CheckBox


def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.elements.check_count_elements(9)


def test_count_checkbox(browser):
    checkbox_page = CheckBox(browser)
    checkbox_page.visit()

    assert checkbox_page.btn_checkbox.check_count_elements(1)
    checkbox_page.btn_plus_checkbox.click()
    assert checkbox_page.btn_checkbox.check_count_elements(17)

    for element in checkbox_page.btn_checkbox.find_elements():
        assert element.is_displayed()

    browser.refresh()
    assert checkbox_page.btn_checkbox.check_count_elements(1)
