class SearchPage:
    def __init__ (self, page):
        self.page = page
        self.origem = page.locator('div.border-e:nth-child(1) > div:nth-child(2) > input:nth-child(2)')
        self.first_origem = page.locator('li.px-5:nth-child(1)')
        self.destino = page.locator('div.border-e:nth-child(2) > div:nth-child(2) > input:nth-child(2)')
        self.first_destino = page.locator('div.absolute:nth-child(3) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1)')
        self.buscar_button = page.get_by_text("Buscar", exact=True)


    def goto(self, url):
        self.page.goto(url)

    def search(self, origem, destino):
        self.origem.fill(origem)
        self.first_origem.click()
        self.destino.fill(destino)
        self.first_destino.click()
        self.buscar_button.click()

    