from playwright.sync_api import Page, Playwright, sync_playwright, expect

import pytest


class ChalmersPage:
    page: Page

    def __init__(self, page):
        self.page = page


class ChalmersHeader(ChalmersPage):
    def click_utbildning(self):
        self.page.get_by_role("link", name="Utbildning").click()

    def click_forskning(self):
        self.page.get_by_role("link", name="Forskning").click()

    def click_samverkan(self):
        self.page.get_by_role("link", name="Samverkan").click()


def test_click_forskning(page: Page):
    page.goto("https://www.chalmers.se")
    main_page = ChalmersHeader(page)
    main_page.click_forskning()
    assert page.url == "https://www.chalmers.se/sv/forskning/Sidor/default.aspx"


def test_click_utbildning(page: Page):
    page.goto("https://www.chalmers.se")
    main_page = ChalmersHeader(page)
    main_page.click_utbildning()
    assert page.url == "https://www.chalmers.se/sv/utbildning/Sidor/default.aspx"


def test_click_samverkan(page: Page):
    page.goto("https://www.chalmers.se")
    main_page = ChalmersHeader(page)
    main_page.click_samverkan()
    assert page.url == "https://www.chalmers.se/sv/samverkan/Sidor/default.aspx"


def test_click_sökfält(page: Page):
    page.goto("https://www.chalmers.se")
    page.





# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.chalmers.se/sv/Sidor/default.aspx")
#     with page.expect_popup() as popup_info:
#         page.get_by_role("link", name="Chalmers tekniska högskola officiella facebooksida").click()
#     page1 = popup_info.value
#     page.wait_for_url("https://www.facebook.com/chalmersuniversityoftechnology")
#     page1.get_by_role("button", name="Only allow essential cookies").click()
#     # ---------------------
#     context.close()
#     browser.close()
# with sync_playwright() as playwright:
#     run(playwright)


