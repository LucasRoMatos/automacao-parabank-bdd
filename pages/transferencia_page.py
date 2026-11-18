from pages.base_page import BasePage


class TransferenciaPage(BasePage):
    # menu lateral (confirme com F12 se necessário)
    LINK_TRANSFERIR = "a[href='transfer.htm']"

    # formulário (confirmado na exploração)
    CAMPO_VALOR = "#amount"
    BOTAO_TRANSFERIR = "input[value='Transfer']"

    # resultado (confirme com F12 na tela de sucesso)
    TITULO_RESULTADO = "h1.title"

    def acessar(self):
        self.clicar(self.LINK_TRANSFERIR)

    def transferir(self, valor):
        self.preencher(self.CAMPO_VALOR, valor)
        self.clicar(self.BOTAO_TRANSFERIR)
        self.page.wait_for_load_state()

    def titulo_resultado(self):
        return self.texto_de(self.TITULO_RESULTADO)

    def texto_resultado(self):
        return self.texto_de("#rightPanel")