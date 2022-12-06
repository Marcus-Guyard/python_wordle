from playwright.sync_api import Playwright, sync_playwright, expect

import time
import random


class Betsspace:

    def __init__(self, page):
        self.page = page

    def home_page(self):
        self.page.goto("/")

    def nav_product_page(self):
        self.page.locator("#Collection > ul > li:nth-child(1) > div > a").click()

    def add_product_to_cart(self):
        self.page.locator("#product_form_6866716590279 > div.product-form__controls-group.product-form__controls-group--submit > div > button").click()

    def remove_product_from_cart(self):
        self.page.locator("#shopify-section-cart-template > div > div:nth-child(1) > form > table > tbody > tr > td.cart__meta.small--text-left > div > div:nth-child(2) > p > a").click()

    def nav_checkout(self):
        self.page.locator("#shopify-section-cart-template > div > div:nth-child(1) > form > div > div > div > div.cart__buttons-container > div.cart__submit-controls > input").click()

    def nav_contact_us(self):
        self.page.goto("/")
        self.page.locator("#shopify-section-footer > footer > div:nth-child(3) > div > div:nth-child(1) > div > ul > li:nth-child(5) > a").click()

    def change_currency(self):
        for n in range(3):
            random_currency = random.randint(1, 111)
            random_currency_name = self.page.text_content(f"#currency-list > li:nth-child({random_currency}) > a")
            print(random_currency_name)
            time.sleep(2)
            self.page.click("#localization_form > div > div > button")
            self.page.click(f"#currency-list > li:nth-child({random_currency}) > a")

    def filter_products(self, option: str):
        self.page.locator("#shopify-section-collection-template").get_by_role("combobox", name="Sort by").select_option(f"{option}")


class BetsspaceHeader(Betsspace):
    def click_logo(self):
        self.page.locator("#shopify-section-header > div > header.small--hide.site-header.logo--left > h1 > a").click()

    def nav_headers(self, tab: str):
        self.page.locator("#shopify-section-header").get_by_role("link", name=f"{tab}").click()

    def click_all_cushions(self):
        self.nav_headers("All Cushions")

    def nav_cart_page(self):
        self.page.get_by_role("link", name="Cart").click()
