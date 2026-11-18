Feature: Login do ParaBank

  Scenario: Login com credenciais incorretas
    Given que abro a página inicial
    When informo o usuário "UserTesteErro" e a senha "SenhaTesteErro"
    Then vejo a mensagem de erro "The username and password could not be verified."