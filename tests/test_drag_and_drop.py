from selenium.webdriver import ActionChains
from pages.droppable import Droppable
import time


def test_drag_and_drop(browser):
    drop_page = Droppable(browser)
    action_chains = ActionChains(browser)

    drop_page.visit()
    assert drop_page.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(
        drop_page.drag.find_element(),
        drop_page.drop.find_element()
    ).perform()
    time.sleep(2)
    assert drop_page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(1)
    action_chains.drag_and_drop_by_offset(drop_page.drag.find_element(), -200, 0
    ).perform()

    time.sleep(1)
    assert drop_page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')