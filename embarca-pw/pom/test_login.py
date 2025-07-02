from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
# import config
import time
import pytest
from pageObjects.LoginPage import LoginPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()

