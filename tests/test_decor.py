from pages.radio_button import Radio
from pages.demoqa import DemoQA
import pytest


@pytest.mark.skip
def test_decor(browser):
    demo = DemoQA(browser)
    demo.visit()

    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_new(browser):
    radio = Radio(browser)

    if not radio.code_status():
        pytest.skip(reason=f'Страница {radio.base_url} недоступна')

    radio.visit()
    radio.yes.click_force()
    assert radio.text.get_text == "You have selected Yes"
    radio.impressive.click_force()
    assert radio.text.get_text == "You have selected Impressive"

    assert 'disabled' in radio.no.get_dom_attribute('class')
