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

    # def test_incorrect_login(self, page: Page):
    #     page.goto("https://www.embarca.ai")
    #     locator = page.get_by_text("Entrar", exact=True)
    #     locator.hover()
    #     locator.click()
    #     page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...").first.fill(config.wrong_email)
    #     page.get_by_placeholder("Insira sua senha...").first.fill(config.wrong_password)
    #     page.locator("button.cursor-pointer:nth-child(3)").click()
    #     time.sleep(2)
    

    # def test_correct_login(self, page: Page):
    #     page.goto("https://www.embarca.ai")
    #     locator = page.get_by_text("Entrar", exact=True)
    #     locator.hover()
    #     locator.click()
    #     page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...").first.fill(config.right_email)
    #     page.get_by_placeholder("Insira sua senha...").first.fill(config.right_password)
    #     page.locator("button.cursor-pointer:nth-child(3)").click()
    #     time.sleep(2)

    def test_search_ticket(self, page: Page):
        page.goto("https://www.embarca.ai")
        # locator = page.get_by_text("Entrar", exact=True)
        # locator.hover()
        # locator.click()
        # page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...").first.fill(config.right_email)
        # page.get_by_placeholder("Insira sua senha...").first.fill(config.right_password)
        # page.locator("button.cursor-pointer:nth-child(3)").click()
        page.locator('div.border-e:nth-child(1) > div:nth-child(2) > input:nth-child(2)').fill(config.origem)
        time.sleep(2)
        page.locator('li.px-5:nth-child(1)').click() #select first option in list
        time.sleep(2)
        page.locator('div.border-e:nth-child(2) > div:nth-child(2) > input:nth-child(2)').fill(config.destino)
        time.sleep(2)
        page.locator('li.px-5:nth-child(1)').click() 
        page.locator("div.border-e:nth-child(3) > div:nth-child(2) > input:nth-child(2)").click() #ida
        page.get_by_text('12').click()
        time.sleep(3)
