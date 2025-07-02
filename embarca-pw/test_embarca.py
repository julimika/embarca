from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import config
import time
import pytest

# def test_has_title(page: Page):
#     page.goto("https://www.embarca.ai")
#     expect(page).to_have_title("Passagem de Ônibus sem sair de casa | Embarca.ai")
#     page.close()

class TestLogin:

    def test_incorrect_login(self, page: Page):
        page.goto("https://www.embarca.ai")
        locator = page.get_by_text("Entrar", exact=True)
        locator.hover()
        locator.click()
        page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...").first.fill(config.wrong_email)
        page.get_by_placeholder("Insira sua senha...").first.fill(config.wrong_password)
        time.sleep(2)
    

    # def test_correct_login(self, page: Page):
    #     page.goto("https://www.embarca.ai")
    #     locator = page.get_by_text("Entrar", exact=True)
    #     locator.hover()
    #     locator.click()
    #     page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...").first.fill(config.right_email)
    #     page.get_by_placeholder("Insira sua senha...").first.fill(config.right_password)
    #     page.locator("div.cursor-pointer:has-text('Login')").click()
    #     time.sleep(2)

# def test_search_ticket(page: Page):
#     page.goto("https://www.embarca.ai")
#     button = page.locator('#adopt-accept-all-button')
#     button.click()
#     locator = page.get_by_text("Entrar", exact=True)
#     locator.hover()
#     locator.click()
#     page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...").first.fill(config.right_email)
#     page.get_by_placeholder("Insira sua senha...").first.fill(config.right_password)
#     page.locator("div.cursor-pointer:has-text('Login')").click()
#     time.sleep(2)
    # page.locator('id=origin_date').hover()
    # fill(config.date)









