from behave import given
from pages.login_page import LoginPage


@given('que abro a página inicial')
def passo_abrir_pagina_inicial(context):
    context.login = LoginPage(context.page)
    context.login.abrir()