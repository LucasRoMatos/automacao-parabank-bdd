from pages.base_page import BasePage
from config import BASE_URL


class RegistroPage(BasePage):
    CAMPO_PRIMEIRO_NOME = "input[name='customer.firstName']"
    CAMPO_ULTIMO_NOME = "input[name='customer.lastName']"
    CAMPO_ENDERECO = "input[name='customer.address.street']"
    CAMPO_CIDADE = "input[name='customer.address.city']"
    CAMPO_ESTADO = "input[name='customer.address.state']"
    CAMPO_CEP = "input[name='customer.address.zipCode']"
    CAMPO_TELEFONE = "input[name='customer.phoneNumber']"
    CAMPO_SSN = "input[name='customer.ssn']"
    CAMPO_NOME_USUARIO = "input[name='customer.username']"
    CAMPO_SENHA = "input[name='customer.password']"
    CAMPO_CONFIRMA_SENHA = "input[name='repeatedPassword']"
    BOTAO_REGISTRAR = "input[value='Register']"
    MENSAGEM_SUCESSO = "#rightPanel p"
    MENSAGENS_DE_ERRO = "span.error" 

    def abrir(self):
        self.page.goto(f"{BASE_URL}/register.htm")

    def preencher_formulario(self, dados):
        mapeamento = {
            "primeiro_nome": self.CAMPO_PRIMEIRO_NOME,
            "ultimo_nome": self.CAMPO_ULTIMO_NOME,
            "endereco": self.CAMPO_ENDERECO,
            "cidade": self.CAMPO_CIDADE,
            "estado": self.CAMPO_ESTADO,
            "cep": self.CAMPO_CEP,
            "telefone": self.CAMPO_TELEFONE,
            "ssn": self.CAMPO_SSN,
            "usuario": self.CAMPO_NOME_USUARIO,
            "senha": self.CAMPO_SENHA,
            "confirma_senha": self.CAMPO_CONFIRMA_SENHA,
        }
        for campo, valor in dados.items():
            self.preencher(mapeamento[campo], valor)

    def enviar(self):
        self.clicar(self.BOTAO_REGISTRAR)
        self.page.wait_for_load_state()

    def mensagem_de_sucesso(self):
        return self.texto_de(self.MENSAGEM_SUCESSO)

    def mensagens_de_erro(self):
        self.page.wait_for_selector(self.MENSAGENS_DE_ERRO)
        return self.page.locator(self.MENSAGENS_DE_ERRO).all_inner_texts()