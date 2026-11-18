from behave import given, then

@given('que abro a página inicial')
def passo_abrir(context):
    context.page.goto("https://parabank.parasoft.com/parabank/index.htm")

@then('vejo o título "{titulo}"')
def passo_titulo(context, titulo):
    assert titulo == context.page.title()