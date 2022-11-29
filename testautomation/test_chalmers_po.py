from __future__ import annotations

from selenium import webdriver

import pytest
import time

from selenium.webdriver.remote.webelement import WebElement

from chalmers_pages import ChalmersHeader, ChalmersFooter, ChalmersUtbildning

RESOLUTIONS = ((1920, 1080),)
RESOLUTIONS2 = ((1920, 1080), (2560, 1448))
INCOGNITO = True
HEADLESS = True


class ChromeWithMem(webdriver.Chrome):
    last_element: WebElement

    def find_element(self, *args, **kwargs) -> WebElement:
        self.last_element = super(webdriver.Chrome, self).find_element(*args, **kwargs)
        return self.last_element


class EdgeWithMem(webdriver.Edge):
    last_element: WebElement

    def find_element(self, *args, **kwargs) -> WebElement:
        self.last_element = super(webdriver.Edge, self).find_element(*args, **kwargs)
        return self.last_element


def get_chrome():
    options = webdriver.ChromeOptions()
    if INCOGNITO:
        options.add_argument("--incognito")
    if HEADLESS:
        options.add_argument("--headless")
    return ChromeWithMem(options=options)


def get_edge():
    options = webdriver.EdgeOptions()
    if INCOGNITO:
        options.add_argument("--incognito")
    if HEADLESS:
        options.add_argument("--headless")
    return EdgeWithMem(options=options)

BROWSERS = [get_chrome]


@pytest.fixture(params=BROWSERS, scope="module")
def driver(request):
    driver_maker = request.param
    d = driver_maker()
    yield d
    d.quit()


@pytest.fixture(params=RESOLUTIONS, scope="module")
def browser(driver, request):
    x, y = request.param
    driver.set_window_position(0, 0)
    driver.set_window_size(x, y)
    yield driver


def test_property_title(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)
    utbildning = main_page.click_utbildning()
    assert utbildning.title == "Hello"


def test_chalmers_header_utbildning(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)

    main_page.click_utbildning()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/default.aspx"


def test_chalmers_header_forskning(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)

    main_page.click_forskning()
    assert browser.current_url == "https://www.chalmers.se/sv/forskning/Sidor/default.aspx"


def test_chalmers_header_samverkan(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)

    main_page.click_samverkan()
    assert browser.current_url == "https://www.chalmers.se/sv/samverkan/Sidor/default.aspx"


def test_chalmers_header_om_chalmers(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)

    main_page.click_om_chalmers()
    assert browser.current_url == "https://www.chalmers.se/sv/om-chalmers/Sidor/default.aspx"


def test_chalmers_header_sökfält(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)

    main_page.click_sökfält("informationsteknik")
    assert browser.current_url == "https://www.chalmers.se/sv/sok/Sidor/default.aspx?q=informationsteknik"


def test_chalmers_header_hem(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)

    main_page.click_hem()
    browser.save_screenshot("foo.png")
    assert browser.current_url == "https://www.chalmers.se/sv/Sidor/default.aspx"


def test_ändra_språk(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(browser)

    main_page.click_språk()
    assert browser.current_url == "https://www.chalmers.se/en/Pages/default.aspx"


def test_utbildning_left_nav_container(browser):
    browser.get("https://www.chalmers.se/sv/utbildning/Sidor/default.aspx")
    utbildning = ChalmersUtbildning(browser)

    utbildning.click_program_grundnivå()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/default.aspx"

    utbildning.click_tekniska_basår()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/tekniska-basar/Sidor/default.aspx"

    utbildning.click_masterprogram()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/masterprogram/Sidor/default.aspx"

    utbildning.click_senare_del_av_program()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/byta-till-chalmers-senare-del-av-program.aspx"

    utbildning.click_fort_och_vidareutbildning()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/vidareutbildning/Sidor/default.aspx"

    utbildning.skrolla(0, 400)
    utbildning.click_öppna_nätbaserade_kurser()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/mooc/Sidor/default.aspx"

    utbildning.click_anmälan_behörighet_och_antagning()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/sa-soker-du-till-chalmers/Sidor/default.aspx"

    utbildning.skrolla(0, 800)
    utbildning.click_program_möt_chalmers()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/mot-chalmers/Sidor/default.aspx"

    utbildning.skrolla(0, 400)
    utbildning.click_att_studera_på_chalmers()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/att-studera-pa-chalmers/Sidor/default.aspx"

    utbildning.skrolla(0, 800)
    utbildning.click_nyheter_om_utbildning_på_chalmers()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/Nyheter-om-utbildning-pa-Chalmers.aspx"

    utbildning.click_hitta_till_chalmers()
    assert browser.current_url == "https://www.chalmers.se/sv/om-chalmers/Sidor/Hitta-till-Chalmers.aspx"
    utbildning.backa()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/Nyheter-om-utbildning-pa-Chalmers.aspx"

    utbildning.skrolla(0, 400)
    utbildning.click_kontakt_för_studiefrågor()
    assert browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/kontakt.aspx"


def test_links_facebook(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersFooter(browser)

    main_page.skrolla(0, 4000)
    main_page.click_facebook()


def test_links_instagram(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersFooter(browser)

    main_page.skrolla(0, 4000)
    main_page.click_instagram()


def test_links_twitter(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersFooter(browser)

    main_page.skrolla(0, 4000)
    main_page.click_twitter()


def test_links_youtube(browser):
    browser.get("https://www.chalmers.se")
    main_page = ChalmersFooter(browser)

    main_page.skrolla(0, 4000)
    main_page.click_youtube()
