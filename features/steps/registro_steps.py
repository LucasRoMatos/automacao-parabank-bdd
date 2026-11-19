from behave import given, when, then, step
from pages.registro_page import RegistroPage
from support.dados import novo_usuario


@step('que abro a página de registro')
def passo_abrir_registro(context):
    context.registro = RegistroPage(context.page)
    context.registro.abrir()


@given('que preparo os dados de um novo usuário')
def passo_preparar_dados(context):
    context.dados = novo_usuario()


@when('preencho o formulário com os dados preparados')
def passo_preencher(context):
    context.registro.preencher_formulario(context.dados)


@when('envio o formulário de registro')
def passo_enviar(context):
    context.registro.enviar()

@when('deixo o campo "{campo}" vazio e envio o formulário')
def passo_campo_vazio(context, campo):
    dados = dict(context.dados)
    del dados[campo]
    context.registro.preencher_formulario(dados)
    context.registro.enviar()

@then('vejo a mensagem de conta criada com sucesso')
def passo_sucesso(context):
    atual = context.registro.mensagem_de_sucesso()
    esperado = "Your account was created successfully. You are now logged in."
    assert esperado == atual, f"Esperado '{esperado}', mas apareceu '{atual}'"

@then('vejo a mensagem de campo obrigatório "{mensagem}"')
def passo_campo_obrigatorio(context, mensagem):
    mensagens = context.registro.mensagens_de_erro()
    assert mensagem in mensagens, f"Esperado '{mensagem}', mas apareceu {mensagens}"

@when('modifico o campo "{campo}" com o valor "{valor}"')
def passo_modifico_campo_por_valor(context, campo, valor):
    dados = dict(context.dados)
    dados[campo] = valor
    context.registro.preencher_formulario(dados)

@then('vejo a mensagem de erro de cadastro "{mensagem}"')
def passo_erro_cadastro(context, mensagem):
    mensagens = context.registro.mensagens_de_erro()
    assert mensagem in mensagens, f"Esperado '{mensagem}', mas apareceu {mensagens}"

