from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.section_content_one.visible()
    accordion_page.section_heading.click()
    time.sleep(2)
    assert not accordion_page.section_content_one.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.section_content_two.visible()
    assert not accordion_page.section_content_two_other.visible()
    assert not accordion_page.section_content_three.visible()
