from behave import given, then

@then('vejo o título "{titulo}"')
def passo_titulo(context, titulo):
    assert titulo == context.page.title()