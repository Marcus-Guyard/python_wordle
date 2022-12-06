import pytest

from playwright.sync_api import Playwright, sync_playwright, expect

from performance_testing.playwright_loadtesting import add_to_cart_load_test

import time
import random
import json


def nav_headers(page, n):
    page.goto("/")
    page.click(f"#SiteNav > li:nth-child({n}) > a > span")


def nav_contact_us(page):
    page.goto("/")
    page.click("#shopify-section-footer > footer > div:nth-child(3) > div > div:nth-child(1) > div > ul > li:nth-child(5) > a")


def click_all_cushions(page):
    nav_headers(page, 3)
    expect(page).to_have_url("https://betsspace.com/collections/cushions")


def add_product_to_cart(page):
    page.click("#Collection > ul > li:nth-child(1) > div > a")
    page.click("#product_form_6866716590279 > div.product-form__controls-group.product-form__controls-group--submit > div > button")
    time.sleep(2)
    page.goto("/cart")


def test_click_betsspace_logo(page):
    page.goto("/")
    page.click("text=BETS SPACE")
    expect(page).to_have_url("https://betsspace.com/")


def test_click_sale(page):
    nav_headers(page, 1)
    expect(page).to_have_url("https://betsspace.com/collections/sale")


def test_click_new_collection(page):
    nav_headers(page, 2)
    expect(page).to_have_url("https://betsspace.com/collections/new-collection")


def test_click_about_us(page):
    nav_headers(page, 4)
    expect(page).to_have_url("https://betsspace.com/pages/about-us")


def test_go_to_cart_page(page):
    page.goto("/")
    page.get_by_role("link", name="Cart").click()
    expect(page).to_have_url("https://betsspace.com/cart")


def test_go_to_product_page(page):
    click_all_cushions(page)
    page.click("#Collection > ul > li:nth-child(1) > div > a")
    time.sleep(2)
    assert page.url.startswith("https://betsspace.com/collections/cushions/products/")


def test_add_product_to_cart(page):
    click_all_cushions(page)
    page.click("#Collection > ul > li:nth-child(1) > div > a")
    product_name = page.text_content("#ProductSection-product-template > div > div.grid__item.product-desc-container.medium-up--one-half > div.product-single__meta > h1")
    page.locator("#product_form_6866716590279 > div.product-form__controls-group.product-form__controls-group--submit > div > button").click()
    time.sleep(2)
    page.goto("/cart")
    added_item = page.locator("#shopify-section-cart-template > div > div:nth-child(1) > form > table > tbody > tr > td.cart__meta.small--text-left > div")
    expect(added_item).to_contain_text(product_name)


def test_remove_item_from_cart(page):
    click_all_cushions(page)
    add_product_to_cart(page)
    page.click("#shopify-section-cart-template > div > div:nth-child(1) > form > table > tbody > tr > td.cart__meta.small--text-left > div > div:nth-child(2) > p > a")
    expect(page.locator("#shopify-section-cart-template > div > div.empty-page-content.text-center > p")).to_contain_text("Your cart is currently empty."), "Empty cart string does not match expected value"


def test_nav_checkout_page(page):
    click_all_cushions(page)
    add_product_to_cart(page)
    page.click("#shopify-section-cart-template > div > div:nth-child(1) > form > div > div > div > div.cart__buttons-container > div.cart__submit-controls > input")

    assert page.url.startswith("https://betsspace.com/checkouts/c/")


def test_nav_contact_us(page):
    nav_contact_us(page)
    time.sleep(2)
    expect(page).to_have_url("https://betsspace.com/pages/contact-us")


def test_currency_change(page):
    page.goto("/")
    currencies = [page.locator(f"#currency-list > li:nth-child({c}) > a") for c in range(1, 111)]
    assert len(currencies) == 110


def test_3_random_currencies(page):
    page.goto("/")
    for n in range(3):
        random_currency = random.randint(1, 111)
        random_currency_name = page.text_content(f"#currency-list > li:nth-child({random_currency}) > a")
        print(random_currency_name)
        time.sleep(2)
        page.click("#localization_form > div > div > button")
        page.click(f"#currency-list > li:nth-child({random_currency}) > a")


def test_filter_best_selling(page):
    click_all_cushions(page)
    time.sleep(2)
    page.get_by_role("combobox", name="Sort by").select_option("best-selling")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=best-selling")


def test_filter_alphabetical_a_z(page):
    click_all_cushions(page)
    time.sleep(2)
    page.get_by_role("combobox", name="Sort by").select_option("title-ascending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=title-ascending")


def test_filter_alphabetical_z_a(page):
    click_all_cushions(page)
    time.sleep(2)
    page.get_by_role("combobox", name="Sort by").select_option("title-descending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=title-descending")


def test_filter_price_low_high(page):
    click_all_cushions(page)
    time.sleep(2)
    page.get_by_role("combobox", name="Sort by").select_option("price-ascending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=price-ascending")


def test_filter_price_high_low(page):
    click_all_cushions(page)
    time.sleep(2)
    page.get_by_role("combobox", name="Sort by").select_option("price-descending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=price-descending")


def test_filter_date_old_new(page):
    click_all_cushions(page)
    time.sleep(2)
    page.get_by_role("combobox", name="Sort by").select_option("created-ascending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=created-ascending")


def test_filter_date_new_old(page):
    click_all_cushions(page)
    time.sleep(2)
    page.get_by_role("combobox", name="Sort by").select_option("created-descending")
    expect(page).to_have_url("https://betsspace.com/collections/cushions?sort_by=created-descending")


def test_contact_us_website_owner_email(page):
    nav_contact_us(page)
    expect(page.locator("#MainContent > div > div > div > div.rte > span")).to_contain_text("info@betsspace.com")


def test_contact_us_customer_email_field(page):
    nav_contact_us(page)
    locator = page.locator("#ContactForm > div > div:nth-child(2)")
    expect(locator).to_contain_text("Email")


def test_contact_us_customer_phone_nr_field(page):
    nav_contact_us(page)
    locator = page.locator("#ContactForm > label:nth-child(4)")
    expect(locator).to_contain_text("Phone Number")


def test_contact_us_customer_name_field(page):
    nav_contact_us(page)
    locator = page.locator("#ContactForm > div > div:nth-child(1)")
    expect(locator).to_contain_text("Name")


def test_add_to_cart_performance(page):
    add_to_cart_load_test(page)
    path = "D:\PycharmProjects\Testautomation_Case\performance_testing\performance_metrics.json"
    with open(path, "r") as f:
        performanceMetrics = json.load(f)
        assert performanceMetrics[29]["value"] < 2
        print(performanceMetrics[29])
        assert performanceMetrics[28]["value"] < 5
        print(performanceMetrics[28])
        assert performanceMetrics[26]["value"] < 5
        print(performanceMetrics[26])

