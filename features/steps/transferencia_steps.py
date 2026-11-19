from behave import given, when, then
from pages.transferencia_page import TransferenciaPage


@given('que acesso a transferência de fundos')
def passo_acessar_transferencia(context):
    context.transferencia = TransferenciaPage(context.page)
    context.transferencia.acessar()


@when('transfiro "{valor}"')
def passo_transferir(context, valor):
    context.transferencia.transferir(valor)


@then('vejo a mensagem de transferência concluída')
def passo_transferencia_concluida(context):
    texto = context.transferencia.texto_resultado()
    assert "Transfer Complete" in texto or "internal error" not in texto.lower(), (
        f"A aplicação retornou erro interno em vez de concluir a transferência: '{texto}'"
    )

@then('vejo a mensagem de erro interno')
def passo_erro_interno(context):
    texto = context.transferencia.texto_resultado()
    assert "internal error" in texto, f"Esperado erro interno, mas a tela mostrou: '{texto}'"

@when('transfiro sem valor')
def passo_transferir_sem_valor(context):
    context.transferencia.transferir("")