from behave import given
from pages.login_page import LoginPage
from pages.registro_page import RegistroPage
from support.dados import novo_usuario


@given('que abro a página inicial')
def passo_abrir_pagina_inicial(context):
    context.login = LoginPage(context.page)
    context.login.abrir()


@given('que existe um usuário cadastrado')
def passo_usuario_cadastrado(context):
    context.dados = novo_usuario()
    registro = RegistroPage(context.page)
    registro.abrir()
    registro.preencher_formulario(context.dados)
    registro.enviar()
    texto = registro.mensagem_de_sucesso()
    assert "created successfully" in texto, (
        f"Cadastro não confirmado. A tela mostrou: '{texto}'"
    )