from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    progress = ProgressBar(browser)
    progress.visit()

    progress.start.click()

    while True:
        if progress.bar.get_dom_attribute('aria-valuenow') == '51':
            progress.start.click()
        break
