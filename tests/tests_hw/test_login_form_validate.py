from pages.form_page import FormPage
import time


def test_login_form_validate(browser):
    valid = FormPage(browser)
    valid.visit()

    assert valid.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert valid.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert valid.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert valid.user_email.get_dom_attribute('pattern') == \
           '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    time.sleep(2)
    browser.set_window_size(width=1000, height=1000)
    time.sleep(2)
    valid.btn_submit.click_force()
    time.sleep(2)
    assert valid.user_form.get_dom_attribute('class') == 'was-validated'
