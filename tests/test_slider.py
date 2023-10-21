from selenium.webdriver.common.keys import Keys
from pages.slider import Slider


def test_slider(browser):
    slider = Slider(browser)
    slider.visit()

    assert slider.btn_slide.exist()
    assert slider.value.exist()

    while not slider.value.get_dom_attribute('value') == '50':
        slider.btn_slide.send_keys(Keys.ARROW_RIGHT)

    assert slider.value.get_dom_attribute('value') == '50'
