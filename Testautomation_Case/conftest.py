import pytest
from playwright.sync_api import BrowserType
from typing import Dict
from slugify import slugify
from pathlib import Path


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": False,
        "viewport": {
            "width": 1500,
            "height": 720,
        }

    }


def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path(".playwright-screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            page.screenshot(path=str(screenshot_dir / f"{slugify(item.nodeid)}.png"))
