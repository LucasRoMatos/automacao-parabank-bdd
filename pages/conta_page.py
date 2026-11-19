from pages.base_page import BasePage


class ContaPage(BasePage):
    LINK_SAIR = "text=Log Out"
    TITULO = "h1[class='title']"

    def sair(self):
        self.clicar(self.LINK_SAIR)

    def titulo(self):
        return self.texto_de(self.TITULO)