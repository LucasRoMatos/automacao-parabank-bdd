class BasePage:
    """Ações comuns que qualquer tela pode usar."""

    def __init__(self, page):
        self.page = page

    def preencher(self, seletor, texto):
        self.page.fill(seletor, texto)

    def clicar(self, seletor):
        self.page.click(seletor)

    def texto_de(self, seletor):
        return self.page.inner_text(seletor)