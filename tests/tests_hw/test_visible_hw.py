from pages.accordian import Accordian
import time


def test_visible_accordion(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert accordian_page.section_content_one.visible()
    accordian_page.section_heading.click()
    time.sleep(2)
    assert not accordian_page.section_content_one.visible()


def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)

    accordian_page.visit()
    assert not accordian_page.section_content_two.visible()
    assert not accordian_page.section_content_two_other.visible()
    assert not accordian_page.section_content_three.visible()
