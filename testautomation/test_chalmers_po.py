from __future__ import annotations

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


@pytest.fixture
def chrome_browser(incognito_window):
    driver = webdriver.Chrome(options=incognito_window)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


class ChalmersPage:
    driver: webdriver.Chrome

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def backa(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def skrolla(self, x: int, y: int):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")


class ChalmersHeader(ChalmersPage):
    def click_hem(self):
        self.driver.find_element(By.ID, "ctl00_ctl34_imgSource").click()

    def click_utbildning(self) -> ChalmersUtbildning:
        self.driver.find_element(By.LINK_TEXT, "Utbildning").click()
        return ChalmersUtbildning(self.driver)

    def click_forskning(self):
        self.driver.find_element(By.LINK_TEXT, "Forskning").click()

    def click_samverkan(self):
        self.driver.find_element(By.LINK_TEXT, "Samverkan").click()

    def click_om_chalmers(self):
        self.driver.find_element(By.LINK_TEXT, "Om Chalmers").click()

    def click_sökfält(self, sökinput: str):
        sökfält = self.driver.find_element(By.ID, "ctl00_ctl44_ctl00_search_all_chalmers_se_sv_field")
        sökfält.send_keys(sökinput)
        sökfält.send_keys(Keys.ENTER)

    def click_språk(self):
        self.driver.find_element(By.LINK_TEXT, "In English").click()


class ChalmersUtbildning(ChalmersPage):
    def click_program_grundnivå(self):
        self.driver.find_element(By.LINK_TEXT, "Program på grundnivå").click()

    def click_tekniska_basår(self):
        self.driver.find_element(By.LINK_TEXT, "Tekniska basår").click()

    def click_masterprogram(self):
        self.driver.find_element(By.LINK_TEXT, "Masterprogram").click()

    def click_senare_del_av_program(self):
        self.driver.find_element(By.LINK_TEXT, "Senare del av program").click()

    def click_fort_och_vidareutbildning(self):
        self.driver.find_element(By.LINK_TEXT, "Fort- och vidareutbildning").click()

    def click_öppna_nätbaserade_kurser(self):
        self.driver.find_element(By.LINK_TEXT, "Öppna nätbaserade kurser (moocar)").click()

    def click_anmälan_behörighet_och_antagning(self):
        self.driver.find_element(By.LINK_TEXT, "Anmälan, behörighet och antagning").click()

    def click_program_möt_chalmers(self):
        self.driver.find_element(By.LINK_TEXT, "Möt Chalmers").click()

    def click_att_studera_på_chalmers(self):
        self.driver.find_element(By.LINK_TEXT, "Att studera på Chalmers").click()

    def click_nyheter_om_utbildning_på_chalmers(self):
        self.driver.find_element(By.LINK_TEXT, "Nyheter om utbildning på Chalmers").click()

    def click_hitta_till_chalmers(self):
        self.driver.find_element(By.LINK_TEXT, "Hitta till Chalmers").click()

    def click_kontakt_för_studiefrågor(self):
        self.driver.find_element(By.LINK_TEXT, "Kontakt för studiefrågor").click()

    @property
    def title(self) -> str:
        return self.driver.find_element(By.XPATH, '//*[@id="ctl00_MSO_ContentDiv"]/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div[2]/h3').text


class ChalmersForskning(ChalmersPage):
    def click_starka_forskningsområden(self):
        self.driver.find_element(By.LINK_TEXT, "Starka forskningsområden").click()

    def click_exempel_på_nytta(self):
        self.driver.find_element(By.LINK_TEXT, "Exempel på nytta från forskning").click()

    def click_klimatforskning(self):
        self.driver.find_element(By.LINK_TEXT, "Klimatforskning").click()

    def click_insatser_och_expertis(self):
        self.driver.find_element(By.LINK_TEXT, "Insatser och expertis kring corona och covid-19").click()

    def click_institutioner(self):
        self.driver.find_element(By.LINK_TEXT, "Institutioner").click()

    def click_forskarutbildning(self):
        self.driver.find_element(By.LINK_TEXT, "Forskarutbildning").click()

    def click_forskningsinfrastruktur(self):
        self.driver.find_element(By.LINK_TEXT, "Forskningsinfrastruktur").click()

    def click_forskningsfinansiering(self):
        self.driver.find_element(By.LINK_TEXT, "Forskningsfinansiering").click()

    def click_forskningsprojekt(self):
        self.driver.find_element(By.LINK_TEXT, "Forskningsprojekt").click()

    def click_centrum(self):
        self.driver.find_element(By.LINK_TEXT, "Centrum").click()

    def click_grafen(self):
        self.driver.find_element(By.LINK_TEXT, "Grafen").click()

    def click_möt_våra_forskare(self):
        self.driver.find_element(By.LINK_TEXT, "Möt våra forskare").click()

    def click_chalmers_på_ted(self):
        self.driver.find_element(By.LINK_TEXT, "Chalmers på TED").click()

    def click_nobelföreläsningar(self):
        self.driver.find_element(By.LINK_TEXT, "Nobelföreläsningar").click()

    def click_populärvetenskap(self):
        self.driver.find_element(By.LINK_TEXT, "Populärvetenskap").click()

    def click_publikationer(self):
        self.driver.find_element(By.LINK_TEXT, "Publikationer").click()

    def click_twitter_chalmers_nyheter(self):
        self.driver.find_element(By.LINK_TEXT, "twitter @chalmersnyheter").click()


class ChalmersSamverkan(ChalmersPage):
    pass


class ChalmersOmChalmers(ChalmersPage):
    pass


def test_property_title(chrome_browser):
    chrome_browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(chrome_browser)
    utbildning = main_page.click_utbildning()
    print(utbildning.title)


def test_chalmers_header(chrome_browser):
    chrome_browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(chrome_browser)

    main_page.click_utbildning()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/default.aspx"

    main_page.click_forskning()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/Sidor/default.aspx"

    main_page.click_samverkan()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/samverkan/Sidor/default.aspx"

    main_page.click_om_chalmers()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/om-chalmers/Sidor/default.aspx"

    main_page.click_sökfält("informationsteknik")
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/sok/Sidor/default.aspx?q=informationsteknik"

    main_page.click_hem()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/Sidor/default.aspx"


def test_ändra_språk(chrome_browser):
    chrome_browser.get("https://www.chalmers.se")
    main_page = ChalmersHeader(chrome_browser)

    main_page.click_språk()
    assert chrome_browser.current_url == "https://www.chalmers.se/en/Pages/default.aspx"


def test_utbildning_left_nav_container(chrome_browser):
    chrome_browser.get("https://www.chalmers.se/sv/utbildning/Sidor/default.aspx")
    utbildning = ChalmersUtbildning(chrome_browser)

    utbildning.click_program_grundnivå()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/program-pa-grundniva/Sidor/default.aspx"

    utbildning.click_tekniska_basår()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/tekniska-basar/Sidor/default.aspx"

    utbildning.click_masterprogram()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/masterprogram/Sidor/default.aspx"

    utbildning.click_senare_del_av_program()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/byta-till-chalmers-senare-del-av-program.aspx"

    utbildning.click_fort_och_vidareutbildning()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/vidareutbildning/Sidor/default.aspx"

    utbildning.click_öppna_nätbaserade_kurser()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/mooc/Sidor/default.aspx"

    utbildning.click_anmälan_behörighet_och_antagning()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/sa-soker-du-till-chalmers/Sidor/default.aspx"

    utbildning.skrolla(0, 800)
    utbildning.click_program_möt_chalmers()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/mot-chalmers/Sidor/default.aspx"

    utbildning.click_att_studera_på_chalmers()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/att-studera-pa-chalmers/Sidor/default.aspx"

    utbildning.skrolla(0, 800)
    utbildning.click_nyheter_om_utbildning_på_chalmers()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/Nyheter-om-utbildning-pa-Chalmers.aspx"

    utbildning.click_hitta_till_chalmers()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/om-chalmers/Sidor/Hitta-till-Chalmers.aspx"
    utbildning.backa()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/Nyheter-om-utbildning-pa-Chalmers.aspx"

    utbildning.click_kontakt_för_studiefrågor()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/utbildning/Sidor/kontakt.aspx"


def test_forskning_left_nav_container(chrome_browser):
    chrome_browser.get("https://www.chalmers.se/sv/forskning/Sidor/default.aspx")
    forskning = ChalmersForskning(chrome_browser)

    forskning.click_starka_forskningsområden()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/starka/Sidor/default.aspx"

    forskning.click_exempel_på_nytta()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/impact/Sidor/default.aspx"

    forskning.click_klimatforskning()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/klimatforskning/Sidor/default.aspx"

    forskning.click_insatser_och_expertis()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/insatser-och-expertis-corona/Sidor/default.aspx"

    forskning.click_institutioner()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/institutioner/Sidor/default.aspx"
    forskning.backa()

    forskning.click_forskarutbildning()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/forskarutbildning/Sidor/default.aspx"

    forskning.skrolla(0, 600)
    forskning.click_forskningsinfrastruktur()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskningsinfrastruktur/Sidor/default.aspx"
    forskning.backa()

    forskning.click_forskningsfinansiering()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/forskningsfinansiering/Sidor/default.aspx"

    forskning.click_forskningsprojekt()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/projekt/Sidor/default.aspx"
    forskning.backa()

    forskning.skrolla(0, 600)
    forskning.click_centrum()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/centrum/Sidor/centrum.aspx"
    forskning.backa()

    forskning.skrolla(0, 600)
    forskning.click_grafen()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/centrum/graphene/Sidor/default.aspx"
    forskning.backa()

    forskning.skrolla(0, 600)
    forskning.click_möt_våra_forskare()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/vara-forskare/Sidor/engagerade-forskare.aspx"

    forskning.skrolla(0, 600)
    forskning.click_chalmers_på_ted()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/chalmers-ted/Sidor/default.aspx"

    forskning.skrolla(0, 600)
    forskning.click_nobelföreläsningar()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/nobelforelasningar/Sidor/Nobelforelasningar.aspx"

    forskning.skrolla(0, 600)
    forskning.click_populärvetenskap()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/popularvetenskap/Sidor/default.aspx"

    forskning.skrolla(0, 600)
    forskning.click_twitter_chalmers_nyheter()
    assert chrome_browser.current_url == "https://www.chalmers.se/sv/forskning/Sidor/twitter.aspx"
