Feature: Login do ParaBank

  Background:
    Given que abro a página inicial

  Scenario: Login com credenciais incorretas
    When informo o usuário "UserTesteErro" e a senha "SenhaTesteErro"
    Then vejo a mensagem de erro "The username and password could not be verified."

  Scenario: Login com senha incorreta para usuário cadastrado
    Given que existe um usuário cadastrado
    And que faço logout
    When informo o usuário cadastrado e a senha "SenhaErrada123"
    Then vejo a mensagem de erro "The username and password could not be verified."

  Scenario Outline: Login com campo vazio
    When informo o usuário "<usuario>" e a senha "<senha>"
    Then vejo a mensagem de erro "Please enter a username and password."

    Examples:
      | usuario | senha    |
      | vazio   | senha123 |
      | usuario | vazio    |
      | vazio   | vazio    |

  Scenario: Login com credenciais corretas
    Given que existe um usuário cadastrado
    And que faço logout
    When informo o usuário cadastrado e sua senha
    Then vejo a página de contas

  Scenario: Logout
    Given que existe um usuário cadastrado
    When que faço logout
    Then vejo a página inicial

  @caracterizacao
  Scenario: Acesso à página de contas sem login retorna erro interno
    Given que existe um usuário cadastrado
    And que faço logout
    When acesso a página de contas diretamente
    Then vejo a mensagem de erro "An internal error has occurred and has been logged."