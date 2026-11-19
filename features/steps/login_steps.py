from behave import given, when, then, step
from pages.login_page import LoginPage
from pages.conta_page import ContaPage
from config import BASE_URL

@when('informo o usuário "{usuario}" e a senha "{senha}"')
def passo_logar(context, usuario, senha):
    usuario = "" if usuario == "vazio" else usuario
    senha = "" if senha == "vazio" else senha
    context.login.logar(usuario, senha)

@then('vejo a mensagem de erro "{mensagem}"')
def passo_mensagem_erro(context, mensagem):
    mensagem_atual = context.login.mensagem_de_erro()
    assert mensagem_atual == mensagem, (
        f"Esperado '{mensagem}', mas apareceu '{mensagem_atual}'"
    )

@step('que faço logout')
def passo_logout(context):
    ContaPage(context.page).sair()

@when('informo o usuário cadastrado e sua senha')
def passo_logar_cadastrado(context):
    context.login.logar(context.dados["usuario"], context.dados["senha"])

@then('vejo a página de contas')
def passo_pagina_de_contas(context):
    titulo = ContaPage(context.page).titulo()
    assert titulo == "Accounts Overview", (
        f"Esperado 'Accounts Overview', mas apareceu '{titulo}'"
    )

@then('vejo a página inicial')
def passo_pagina_inicial(context):
    assert LoginPage(context.page).formulario_visivel(), (
        "Esperado o formulário de login na página inicial"
    )

@when('informo o usuário cadastrado e a senha "{senha}"')
def passo_logar_usuario_cadastrado_senha_errada(context, senha):
    context.login.logar(context.dados["usuario"], senha)

@when('acesso a página de contas diretamente')
def passo_acessar_contas_direto(context):
    context.page.goto(f"{BASE_URL}/overview.htm")