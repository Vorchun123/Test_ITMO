from pages.clear import ClearPage

def test_placeholder(browser):
    placeh = ClearPage(browser)

    placeh.visit()
    assert placeh.full_name.get_dom_attribute('placeholder') == 'Full Name'

