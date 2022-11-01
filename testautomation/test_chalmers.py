from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest

import time


@pytest.fixture
def incognito_window():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    return chrome_options


# 1 öppna en webbläsare och å till www.chalmers.se
# Några problem
# 1. Hårdkodad data i testfunktionen. Exempelvis hur vi hittar olika element. Om systemet vi testar förändras måste vi manuellt rätta varje test
# 2. setup av webläsare och upplösning inne i testfunktionen.
def test_nav_it(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)  # Starta en webbläsare och ge mig en referens till den
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    browser.find_element(By.LINK_TEXT, "Utbildning").click()
    browser.find_element(By.LINK_TEXT, "Program på grundnivå").click()
    browser.find_element(By.LINK_TEXT, "Elektro, Data, IT och Medicinteknik").click()
    browser.find_element(By.CSS_SELECTOR, ".orange li:nth-child(5) .meta").click()


def test_nav_architecture(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    browser.find_element(By.LINK_TEXT, "Utbildning").click()
    browser.find_element(By.LINK_TEXT, "Masterprogram").click()
    browser.find_element(By.LINK_TEXT, "Chalmers 40 masterprogram").click()
    browser.find_element(By.LINK_TEXT, "Architecture").click()
    browser.find_element(By.CSS_SELECTOR, "#EducationArea8 li:nth-child(1) .title").click()
    element = browser.find_element(By.XPATH, '//*[@id="ctl00_PlaceHolderMain_EducationAreaH1CssLookup1"]').text
    assert element == "Architecture and planning beyond sustainability, MSc"


def test_search_bar(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    inputElement = browser.find_element(By.ID, "ctl00_ctl44_ctl00_search_all_chalmers_se_sv_field")
    if browser.get_window_size()["width"] < 991:
        browser.find_element(By.ID, "search-dropdown").click()
        inputElement = browser.find_element(By.ID, "ctl00_ctl46_ctl00_search_all_chalmers_se_sv_field")
    inputElement.send_keys('informationsteknik')
    inputElement.send_keys(Keys.ENTER)
    browser.find_element(By.LINK_TEXT, "Informationsteknik").click()


def test_nav_facebook(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    browser.execute_script("window.scrollTo(0, 4000)")
    browser.find_element(By.ID, "facebook").click()
    time.sleep(20)


def test_nav_instagram(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    browser.execute_script("window.scrollTo(0, 4000)")
    browser.find_element(By.ID, "instagram").click()
    time.sleep(20)


def test_nav_twitter(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    browser.execute_script("window.scrollTo(0, 4000)")
    browser.find_element(By.ID, "twitter").click()
    time.sleep(20)


def test_nav_youtube(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    browser.execute_script("window.scrollTo(0, 4000)")
    browser.find_element(By.ID, "youtube").click()
    time.sleep(20)


def test_nav_linkedin(incognito_window):
    browser = webdriver.Chrome(options=incognito_window)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.chalmers.se")
    browser.execute_script("window.scrollTo(0, 4000)")
    browser.find_element(By.ID, "linkedin").click()
    time.sleep(20)






