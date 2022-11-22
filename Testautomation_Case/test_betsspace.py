import pytest


@pytest.mark.only_browser("chromium")
def test_click_betsspace_logo(page):
    page.goto("/")
    page.click("text=BETS SPACE")
    assert page.url == "https://betsspace.com/"


@pytest.mark.only_browser("chromium")
def test_click_sale(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(1) > a > span")
    assert page.url == "https://betsspace.com/collections/sale"


@pytest.mark.only_browser("chromium")
def test_click_new_collection(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(2) > a > span")
    assert page.url == "https://betsspace.com/collections/new-collection"


@pytest.mark.only_browser("chromium")
def test_click_all_cushions(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    assert page.url == "https://betsspace.com/collections/cushions"


@pytest.mark.only_browser("chromium")
def test_click_about_us(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(4) > a > span")
    assert page.url == "https://betsspace.com/pages/about-us"
