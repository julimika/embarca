class LoginPage:
    def __init__(self, page):
        self.page = page
        self.entrar_button = page.get_by_text("Entrar", exact=True)
        self.email_input = page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...")
        self.password_input = page.get_by_placeholder("Insira sua senha...")
        self.login_button = page.locator("button.cursor-pointer:nth-child(3)")
        # self.error_message = page.locator
        self.exit_button = page.get_by_text("Sair", exact=True)
        self.confirm_exit_button = page.locator('div.bg-white.rounded-lg.p-6.max-w-md.w-full.mx-4.relative.z-50 button:nth-child(2)')
    def goto(self, url):
        self.page.goto(url)

    def login(self, email, password):
        self.entrar_button.click()
        self.email_input.first.fill(email)
        self.password_input.first.fill(password)
        self.login_button.click()


    def logout(self):
        self.exit_button.click()
        # Click the confirmation button in the modal
        self.confirm_exit_button.click()
            

