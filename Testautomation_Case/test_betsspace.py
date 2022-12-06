import pytest

from playwright.sync_api import expect

from performance_testing.playwright_loadtesting import add_to_cart_load_test

import time
import json

from test_betsspace_classes import BetsspaceHeader, Betsspace


@pytest.fixture
def goto_homepage(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    yield driver


@pytest.fixture
def goto_all_cushions(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.click_all_cushions()
    yield driver


@pytest.fixture()
def goto_contact_us(page):
    driver = BetsspaceHeader(page)
    driver.home_page()
    driver.nav_contact_us()
    yield driver


def test_click_betsspace_logo(goto_homepage):
    driver = goto_homepage
    driver.click_logo()
    expect(driver.page).to_have_url("https://betsspace.com/")


def test_click_sale(goto_homepage):
    driver = goto_homepage
    driver.nav_headers("SALE")
    expect(driver.page).to_have_url("https://betsspace.com/collections/sale")


def test_click_new_collection(goto_homepage):
    driver = goto_homepage
    driver.nav_headers("New Collection")
    expect(driver.page).to_have_url("https://betsspace.com/collections/new-collection")


def test_click_all_cushions(goto_all_cushions):
    driver = goto_all_cushions
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions")


def test_click_about_us(goto_homepage):
    driver = goto_homepage
    driver.nav_headers("About Us")
    expect(driver.page).to_have_url("https://betsspace.com/pages/about-us")


def test_nav_cart_page(goto_homepage):
    driver = goto_homepage
    driver.nav_cart_page()
    expect(driver.page).to_have_url("https://betsspace.com/cart")


def test_nav_product_page(goto_all_cushions):
    driver = goto_all_cushions
    driver.nav_product_page()
    assert driver.page.url.startswith("https://betsspace.com/collections/cushions/products/")


def test_add_product_to_cart(goto_all_cushions):
    driver = goto_all_cushions
    driver.nav_product_page()
    product_name = driver.page.text_content("#ProductSection-product-template > div > div.grid__item.product-desc-container.medium-up--one-half > div.product-single__meta > h1")
    driver.add_product_to_cart()
    time.sleep(2)
    driver.page.goto("/cart")
    added_item = driver.page.locator("#shopify-section-cart-template > div > div:nth-child(1) > form > table > tbody > tr > td.cart__meta.small--text-left > div")
    expect(added_item).to_contain_text(product_name)


def test_remove_item_from_cart(goto_all_cushions):
    driver = goto_all_cushions
    driver.nav_product_page()
    driver.add_product_to_cart()
    time.sleep(2)
    driver.page.goto("/cart")
    driver.remove_product_from_cart()
    expect(driver.page.locator("#shopify-section-cart-template > div > div.empty-page-content.text-center > p")).to_contain_text("Your cart is currently empty."), "Empty cart string does not match expected value"


def test_nav_checkout_page(goto_all_cushions):
    driver = goto_all_cushions
    driver.nav_product_page()
    driver.add_product_to_cart()
    time.sleep(2)
    driver.page.goto("/cart")
    driver.nav_checkout()
    assert driver.page.url.startswith("https://betsspace.com/checkouts/c/")


def test_nav_contact_us(goto_contact_us):
    driver = goto_contact_us
    expect(driver.page).to_have_url("https://betsspace.com/pages/contact-us")


def test_currency_change_availability(goto_homepage):
    driver = goto_homepage
    currencies = [driver.page.locator(f"#currency-list > li:nth-child({c}) > a") for c in range(1, 111)]
    assert len(currencies) == 110


def test_3_random_currencies(goto_homepage):
    driver = goto_homepage
    driver.change_currency()


def test_filter_best_selling(goto_all_cushions):
    driver = goto_all_cushions
    time.sleep(2)
    driver.filter_products("best-selling")
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions?sort_by=best-selling")


def test_filter_alphabetical_a_z(goto_all_cushions):
    driver = goto_all_cushions
    time.sleep(2)
    driver.filter_products("title-ascending")
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions?sort_by=title-ascending")


def test_filter_alphabetical_z_a(goto_all_cushions):
    driver = goto_all_cushions
    time.sleep(2)
    driver.filter_products("title-descending")
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions?sort_by=title-descending")


def test_filter_price_low_high(goto_all_cushions):
    driver = goto_all_cushions
    time.sleep(2)
    driver.filter_products("price-ascending")
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions?sort_by=price-ascending")


def test_filter_price_high_low(goto_all_cushions):
    driver = goto_all_cushions
    time.sleep(2)
    driver.filter_products("price-descending")
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions?sort_by=price-descending")


def test_filter_date_old_new(goto_all_cushions):
    driver = goto_all_cushions
    time.sleep(2)
    driver.filter_products("created-ascending")
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions?sort_by=created-ascending")


def test_filter_date_new_old(goto_all_cushions):
    driver = goto_all_cushions
    time.sleep(2)
    driver.filter_products("created-descending")
    expect(driver.page).to_have_url("https://betsspace.com/collections/cushions?sort_by=created-descending")


def test_contact_us_website_owner_email(goto_contact_us):
    driver = goto_contact_us
    expect(driver.page.locator("#MainContent > div > div > div > div.rte > span")).to_contain_text("info@betsspace.com")


def test_contact_us_customer_email_field(goto_contact_us):
    driver = goto_contact_us
    expect(driver.page.locator("#ContactForm > div > div:nth-child(2)")).to_contain_text("Email")


def test_contact_us_customer_phone_nr_field(goto_contact_us):
    driver = goto_contact_us
    expect(driver.page.locator("#ContactForm > label:nth-child(4)")).to_contain_text("Phone Number")


def test_contact_us_customer_name_field(goto_contact_us):
    driver = goto_contact_us
    expect(driver.page.locator("#ContactForm > div > div:nth-child(1)")).to_contain_text("Name")


@pytest.mark.only_browser("chromium")
def test_add_to_cart_performance(page):
    add_to_cart_load_test(page)
    path = "D:\\PycharmProjects\\Testautomation_Case\\performance_testing\\performance_metrics.json"
    with open(path, "r") as f:
        performancemetrics = json.load(f)
        assert performancemetrics[29]["value"] < 2
        print(performancemetrics[29])
        assert performancemetrics[28]["value"] < 5
        print(performancemetrics[28])
        assert performancemetrics[26]["value"] < 5
        print(performancemetrics[26])
