from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    login = LoginPage(pagina)
    login.abrir()
    login.logar("tomsmith", "senha_errada")
    input("Veja a tela e aperte Enter para fechar...")
    navegador.close()