Feature: Registro do ParaBank

  Background:
    Given que abro a página de registro

  Scenario: Registro com dados válidos
    Given que preparo os dados de um novo usuário
    When preencho o formulário com os dados preparados
    And envio o formulário de registro
    Then vejo a mensagem de conta criada com sucesso

  Scenario: Registro sem telefone
    Given que preparo os dados de um novo usuário
    When deixo o campo "telefone" vazio e envio o formulário
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

  Scenario: Cadastro com senha e confirmação de senha diferente
    Given que preparo os dados de um novo usuário
    When modifico o campo "confirma_senha" com o valor "SenhaDiferente"
    And envio o formulário de registro
    Then vejo a mensagem de erro de cadastro "Passwords did not match."

  Scenario: Cadastro com usuário já existente
    Given que preparo os dados de um novo usuário
    When preencho o formulário com os dados preparados
    And envio o formulário de registro
    And que faço logout
    And que abro a página de registro
    And preencho o formulário com os dados preparados
    And envio o formulário de registro
    Then vejo a mensagem de erro de cadastro "This username already exists."