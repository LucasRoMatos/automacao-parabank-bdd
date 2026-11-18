Feature: Registro do ParaBank

  Background:
    Given que abro a página de registro

  Scenario: Registro com dados válidos
    Given que preparo os dados de um novo usuário
    When preencho o formulário com os dados preparados
    And envio o formulário de registro
    Then vejo a mensagem de conta criada com sucesso

  Scenario Outline: Campo obrigatório vazio impede o registro
    Given que preparo os dados de um novo usuário
    When deixo o campo "<campo>" vazio e envio o formulário
    Then vejo a mensagem de campo obrigatório "<mensagem>"

    Examples:
      | campo         | mensagem                            |
      | primeiro_nome | First name is required.             |
      | ultimo_nome   | Last name is required.              |
      | endereco      | Address is required.                |
      | cidade        | City is required.                   |
      | estado        | State is required.                  |
      | cep           | Zip Code is required.               |
      | ssn           | Social Security Number is required. |
      | usuario       | Username is required.               |
      | senha         | Password is required.               |
      | confirma_senha | Password confirmation is required. |