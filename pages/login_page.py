class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.get_by_placeholder("Insira aqui seu e-mail, CPF ou CNPJ...")
        self.password_input = page.get_by_placeholder("Insira sua senha...")
        self.login_button = page.locator("button.cursor-pointer:nth-child(3)")
        # self.error_message = page.locator

    def goto(self, url):
        self.page.goto(url)

    def login(self, email, password):
        self.email_input.first.fill(email)
        self.password_input.first.fill(password)
        self.login_button.click()       