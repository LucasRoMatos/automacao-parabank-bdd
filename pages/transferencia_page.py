from pages.base_page import BasePage


class TransferenciaPage(BasePage):
    LINK_TRANSFERIR = "a[href='transfer.htm']"
    CAMPO_VALOR = "#amount"
    BOTAO_TRANSFERIR = "input[value='Transfer']"
    TITULO_RESULTADO = "h1.title"

    def acessar(self):
        self.clicar(self.LINK_TRANSFERIR)

    def transferir(self, valor):
        self.preencher(self.CAMPO_VALOR, valor)
        self.clicar(self.BOTAO_TRANSFERIR)
        self.page.wait_for_function(
            "() => {"
            "  const texto = document.body.innerText;"
            "  return !texto.includes('Transfer Funds')"
            "    || texto.includes('Transfer Complete')"
            "    || texto.includes('internal error');"
            "}",
            timeout=15000,
        )
    def titulo_resultado(self):
        return self.texto_de(self.TITULO_RESULTADO)

    def texto_resultado(self):
        return self.texto_de("#rightPanel")