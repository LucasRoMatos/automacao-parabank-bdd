from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):
    # seletores
    CAMPO_USUARIO = "input[name='username']"  
    CAMPO_SENHA = "input[name='password']"     
    BOTAO_ENTRAR = "input[value='Log In']"   

    def abrir(self):
        # navega até a página inicial, onde fica o login
        self.page.goto(BASE_URL)

    def logar(self, usuario, senha):
        self.preencher(self.CAMPO_USUARIO, usuario)
        self.preencher(self.CAMPO_SENHA, senha)
        self.clicar(self.BOTAO_ENTRAR)