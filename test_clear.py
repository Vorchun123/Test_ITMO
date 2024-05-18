import time
from pages.clear import ClearPage

def test_clear(browser):
    clear_page = ClearPage(browser)

    clear_page.visit()
    clear_page.full_name.send_keys('Ivan')
    time.sleep(2)
    clear_page.full_name.clear()
    time.sleep(2)
    assert clear_page.full_name.get_text() == ''

