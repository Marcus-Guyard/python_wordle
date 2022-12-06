import pytest

from playwright.sync_api import Playwright, sync_playwright, expect

from performance_testing.playwright_loadtesting import add_to_cart_load_test

import time
import random
import json


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
        expect(self.page).to_have_url("https://betsspace.com/collections/cushions")

    def nav_cart_page(self):
        self.page.get_by_role("link", name="Cart").click()


def test_click_betsspace_logo(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_logo()
    expect(driver.page).to_have_url("https://betsspace.com/")


def test_click_sale(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_headers("SALE")
    expect(driver.page).to_have_url("https://betsspace.com/collections/sale")


def test_click_new_collection(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_headers("New Collection")
    expect(driver.page).to_have_url("https://betsspace.com/collections/new-collection")


def test_click_all_cushions(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions")


def test_click_about_us(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_headers("About Us")
    expect(driver.page).to_have_url("https://betsspace.com/pages/about-us")


def test_nav_cart_page(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_cart_page()
    expect(page).to_have_url("https://betsspace.com/cart")


def test_nav_product_page(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    driver.nav_product_page()
    assert page.url.startswith("https://betsspace.com/collections/cushions/products/")


def test_add_product_to_cart(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    driver.nav_product_page()
    product_name = driver.page.text_content("#ProductSection-product-template > div > div.grid__item.product-desc-container.medium-up--one-half > div.product-single__meta > h1")
    driver.add_product_to_cart()
    time.sleep(2)
    driver.page.goto("/cart")
    added_item = page.locator("#shopify-section-cart-template > div > div:nth-child(1) > form > table > tbody > tr > td.cart__meta.small--text-left > div")
    expect(added_item).to_contain_text(product_name)


def test_remove_item_from_cart(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    driver.nav_product_page()
    driver.add_product_to_cart()
    time.sleep(2)
    driver.page.goto("/cart")
    driver.remove_product_from_cart()
    expect(driver.page.locator("#shopify-section-cart-template > div > div.empty-page-content.text-center > p")).to_contain_text("Your cart is currently empty."), "Empty cart string does not match expected value"


def test_nav_checkout_page(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    driver.nav_product_page()
    driver.add_product_to_cart()
    time.sleep(2)
    driver.page.goto("/cart")
    driver.nav_checkout()
    assert page.url.startswith("https://betsspace.com/checkouts/c/")


def test_nav_contact_us(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_contact_us()
    expect(driver.page).to_have_url("https://betsspace.com/pages/contact-us")


def test_currency_change_availability(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    currencies = [page.locator(f"#currency-list > li:nth-child({c}) > a") for c in range(1, 111)]
    assert len(currencies) == 110


def test_3_random_currencies(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.change_currency()


def test_filter_best_selling(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    time.sleep(2)
    driver.filter_products("best-selling")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=best-selling")

def test_filter_alphabetical_a_z(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    time.sleep(2)
    driver.filter_products("title-ascending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=title-ascending")


def test_filter_alphabetical_z_a(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    time.sleep(2)
    driver.filter_products("title-descending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=title-descending")


def test_filter_price_low_high(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    time.sleep(2)
    driver.filter_products("price-ascending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=price-ascending")


def test_filter_price_high_low(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    time.sleep(2)
    driver.filter_products("price-descending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=price-descending")


def test_filter_date_old_new(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    time.sleep(2)
    driver.filter_products("created-ascending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=created-ascending")


def test_filter_date_new_old(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    time.sleep(2)
    driver.filter_products("created-descending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=created-descending")


def test_contact_us_website_owner_email(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_contact_us()
    expect(driver.page.locator("#MainContent > div > div > div > div.rte > span")).to_contain_text("info@betsspace.com")


def test_contact_us_customer_email_field(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_contact_us()
    expect(driver.page.locator("#ContactForm > div > div:nth-child(2)")).to_contain_text("Email")


def test_contact_us_customer_phone_nr_field(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_contact_us()
    expect(driver.page.locator("#ContactForm > label:nth-child(4)")).to_contain_text("Phone Number")


def test_contact_us_customer_name_field(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_contact_us()
    expect(driver.page.locator("#ContactForm > div > div:nth-child(1)")).to_contain_text("Name")


def test_add_to_cart_performance(playwright: Playwright):
    add_to_cart_load_test(playwright)
    path = "D:\PycharmProjects\Testautomation_Case\performance_testing\performance_metrics.json"
    with open(path, "r") as f:
        performanceMetrics = json.load(f)
        assert performanceMetrics[29]["value"] < 2
        print(performanceMetrics[29])
        assert performanceMetrics[28]["value"] < 5
        print(performanceMetrics[28])
        assert performanceMetrics[26]["value"] < 5
        print(performanceMetrics[26])


