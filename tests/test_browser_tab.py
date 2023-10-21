from pages.browser_tab import BrowserTab
import time


def test_browser_teb(browser):
    browser_tab_page = BrowserTab(browser)
    browser_tab_page.visit()
    assert len(browser.window_handles) == 1
    browser_tab_page.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
