from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages import config
import time
import pytest

def test_correct_login(page):
    login_page = LoginPage(page)
    login_page.goto("https://embarca.ai")
    login_page.login(config.right_email , config.right_password)
    time.sleep(2)

def test_error_login(page):
    login_page = LoginPage(page)
    login_page.goto("https://embarca.ai")
    time.sleep(2)
    login_page.login(config.wrong_email , config.wrong_password)
    time.sleep(2)    

