from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):
    # seletores
    CAMPO_USUARIO = "input[name='username']"  
    CAMPO_SENHA = "input[name='password']"     
    BOTAO_ENTRAR = "input[value='Log In']"  
    MENSAGEM_ERRO_CREDENCIAIS = "p[class='error']" 

    def abrir(self):
        # navega até a página inicial, onde fica o login
        self.page.goto(f"{BASE_URL}/index.htm")

    def logar(self, usuario, senha):
        self.preencher(self.CAMPO_USUARIO, usuario)
        self.preencher(self.CAMPO_SENHA, senha)
        self.clicar(self.BOTAO_ENTRAR)

    def mensagem_de_erro(self):
        return self.texto_de(self.MENSAGEM_ERRO_CREDENCIAIS)