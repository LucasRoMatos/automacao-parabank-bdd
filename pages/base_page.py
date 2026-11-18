class BasePage:
    """Ações comuns que qualquer tela pode usar."""

    def __init__(self, page):
        # guarda a aba do navegador que esta página vai controlar
        self.page = page

    def preencher(self, seletor, texto):
        # digita o texto no campo indicado pelo seletor
        self.page.fill(seletor, texto)

    def clicar(self, seletor):
        # clica no elemento indicado pelo seletor
        self.page.click(seletor)

    def texto_de(self, seletor):
        # devolve o texto visível do elemento
        return self.page.inner_text(seletor)