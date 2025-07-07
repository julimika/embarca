
    # def test_search_ticket(self, page: Page):
    #     page.goto("https://www.embarca.ai")
    #     # locator = page.get_by_text("Entrar", exact=True)
    #     # locator.hover()
    #     # locator.click()
    #     # page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...").first.fill(config.right_email)
    #     # page.get_by_placeholder("Insira sua senha...").first.fill(config.right_password)
    #     # time.sleep(2)
    #     # page.locator("button.cursor-pointer:nth-child(3)").click()
    #     page.locator('div.border-e:nth-child(1) > div:nth-child(2) > input:nth-child(2)').fill(config.origem)
    #     time.sleep(2)
    #     page.locator('li.px-5:nth-child(1)').click() #select first option in list
    #     page.locator('div.border-e:nth-child(2) > div:nth-child(2) > input:nth-child(2)').fill(config.destino)
    #     time.sleep(2)
    #     page.locator('div.absolute:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)').click()
    #     time.sleep(2)
    #     page.get_by_text("Buscar", exact=True).click()
    #     time.sleep(2)
    #     #incluir datas junto com a busca
    #     infos_viagem = page.locator('.w-\[80\%\] > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
    #     time.sleep(2)
