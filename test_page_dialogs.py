import time
from pages.modal_dialogs import Modal_dialogs
from pages.demoqa import DemoQa
def test_modal_elements(browser):
    modal_dia = Modal_dialogs(browser)

    modal_dia.visit()
    modal_dia.m_d.find_elements()
    assert modal_dia.m_d.check_count_elements(5)
def test_navigation_modal(browser):
    modal_dialogs = Modal_dialogs(browser)
    check_url = DemoQa(browser)

    modal_dialogs.visit()
    modal_dialogs.refresh()
    time.sleep(2)
    modal_dialogs.icon_m.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert check_url.equal_url()
    assert browser.title =='DEMOQA'
    browser.set_window_size(1000, 1000)


