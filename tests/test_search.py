from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
from pages.search_page import SearchPage
from pages import config
import time
import pytest

def test_search_ticket(page):
    search_page = SearchPage(page)
    search_page.goto("https://embarca.ai")
    search_page.search(config.origem, config.destino)
    time.sleep(8)
    search_page.select_ticket()
    time.sleep(10)
