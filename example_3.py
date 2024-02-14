import pytest

@pytest.mark.smoketest
def test_new(browser):
    browser.get("https://www.ebay.com")
    browser.find_element(By.NAME, "search").send_keys("something")
    browser.find_element(By.NAME, "submit").click()
