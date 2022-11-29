import pytest
import time
from playwright.sync_api import expect


def test_click_betsspace_logo(page):
    page.goto("/")
    page.click("text=BETS SPACE")
    assert page.url == "https://betsspace.com/"


def test_click_sale(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(1) > a > span")
    assert page.url == "https://betsspace.com/collections/sale", "Url does not equal: https://betsspace.com/collections/sale"


def test_click_new_collection(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(2) > a > span")
    assert page.url == "https://betsspace.com/collections/new-collection", "Url does not equal: https://betsspace.com/collections/new-collection"


def test_click_all_cushions(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    assert page.url == "https://betsspace.com/collections/cushions", "Url does not equal: https://betsspace.com/collections/cushions"


def test_click_about_us(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(4) > a > span")
    assert page.url == "https://betsspace.com/pages/about-us", "Url does not equal: https://betsspace.com/pages/about-us"


def test_go_to_cart_page(page):
    page.goto("/")
    page.get_by_role("link", name="Cart").click()
    assert page.url == "https://betsspace.com/cart", "Did not navigate to cart page."


def test_go_to_product_page(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.click("#Collection > ul > li:nth-child(1) > div > a")
    page.expect_response("200")


def test_add_product_to_cart(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.click("#Collection > ul > li:nth-child(1) > div > a")
    product_name = page.text_content("#ProductSection-product-template > div > div.grid__item.product-desc-container.medium-up--one-half > div.product-single__meta > h1")
    page.click("#product_form_6866716590279 > div.product-form__controls-group.product-form__controls-group--submit > div > button")
    page.wait_for_load_state()
    page.goto("/cart")
    added_item = page.locator("#shopify-section-cart-template > div > div:nth-child(1) > form > table > tbody > tr > td.cart__meta.small--text-left > div")
    expect(added_item).to_contain_text(product_name)


def test_remove_item_from_cart(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.click("#Collection > ul > li:nth-child(1) > div > a")
    page.click("#product_form_6866716590279 > div.product-form__controls-group.product-form__controls-group--submit > div > button")
    page.wait_for_load_state()
    page.goto("/cart")
    page.click("#shopify-section-cart-template > div > div:nth-child(1) > form > table > tbody > tr > td.cart__meta.small--text-left > div > div:nth-child(2) > p > a")
    expect(page.locator("#shopify-section-cart-template > div > div.empty-page-content.text-center > p")).to_contain_text("Your cart is currently empty."), "Empty cart string does not match expected value"


def test_nav_checkout_page(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.click("#Collection > ul > li:nth-child(1) > div > a")
    page.click("#product_form_6866716590279 > div.product-form__controls-group.product-form__controls-group--submit > div > button")
    page.wait_for_load_state()
    page.goto("/cart")
    page.click("#shopify-section-cart-template > div > div:nth-child(1) > form > div > div > div > div.cart__buttons-container > div.cart__submit-controls > input")
    assert page.url.startswith("https://betsspace.com/checkouts/c/")


def test_nav_contact_us(page):
    page.goto("/")
    page.click("#shopify-section-footer > footer > div:nth-child(3) > div > div:nth-child(1) > div > ul > li:nth-child(5) > a")
    expect(page).to_have_url("https://betsspace.com/pages/contact-us")


def test_all_currencies(page):
    currencies = []
    for n in range(1, 111):
        page.goto("/")
        page.click("#localization_form > div > div > button")
        page.click(f"#currency-list > li:nth-child({n}) > a")
        currency = page.text_content(f"#currency-list > li:nth-child({n}) > a")
        currencies.append(currency)
    assert len(currencies) == 110


def test_filter_best_selling(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.wait_for_load_state()
    page.get_by_role("combobox", name="Sort by").select_option("best-selling")
    expect(page.locator("#Collection > ul > li:nth-child(1) > div > a")).to_contain_text("Gabrielle Cush")


def test_filter_alphabetical_a_z(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.wait_for_load_state()
    page.get_by_role("combobox", name="Sort by").select_option("title-ascending")
    expect(page.locator("#Collection > ul > li:nth-child(1) > div > a")).to_contain_text("Alice Cush")


def test_filter_alphabetical_z_a(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.wait_for_load_state()
    page.get_by_role("combobox", name="Sort by").select_option("title-descending")
    expect(page.locator("#Collection > ul > li:nth-child(1) > div > a")).to_contain_text("Zoey Cush")


def test_filter_price_low_high(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.wait_for_load_state()
    page.get_by_role("combobox", name="Sort by").select_option("price-ascending")
    expect(page.locator("#Collection > ul > li:nth-child(1) > div > a")).to_contain_text("Tony Cush")


def test_filter_price_high_low(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.wait_for_load_state()
    page.get_by_role("combobox", name="Sort by").select_option("price-descending")
    expect(page.locator("#Collection > ul > li:nth-child(1) > div > a")).to_contain_text("Bridgette Cush")


def test_filter_date_old_new(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.wait_for_load_state()
    page.get_by_role("combobox", name="Sort by").select_option("created-ascending")
    expect(page.locator("#Collection > ul > li:nth-child(1) > div > a")).to_contain_text("Svensson Cush")


def test_filter_date_new_old(page):
    page.goto("/")
    page.click("#SiteNav > li:nth-child(3) > a > span")
    page.wait_for_load_state()
    page.get_by_role("combobox", name="Sort by").select_option("created-descending")
    expect(page.locator("#Collection > ul > li:nth-child(1) > div > a")).to_contain_text("Bobby Cush")
















