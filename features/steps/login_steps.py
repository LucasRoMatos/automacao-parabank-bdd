from behave import given, when, then
from pages.login_page import LoginPage

@when('informo o usuário "{usuario}" e a senha "{senha}"')
def passo_logar(context, usuario, senha):
    context.login.logar(usuario, senha)


@then('vejo a mensagem de erro "{mensagem}"')
def passo_mensagem_erro(context, mensagem):
    mensagem_atual = context.login.mensagem_de_erro()
    assert mensagem_atual == mensagem, (
        f"Esperado '{mensagem}', mas apareceu '{mensagem_atual}'"
    )