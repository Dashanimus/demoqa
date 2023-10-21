from pages.text_box import TextBox
import time


def test_text_clear(browser):
    text_b = TextBox(browser)
    text_b.visit()

    text_b.full_name.send_keys('Scott Cawthon')
    time.sleep(3)

    text_b.full_name.clear()
    time.sleep(3)

    assert text_b.full_name.get_text() == ''
