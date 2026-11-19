Feature: Transferência de fundos

  Background:
    Given que abro a página inicial
    And que existe um usuário cadastrado
    And que acesso a transferência de fundos

  Scenario: Transferência com valor válido
    When transfiro "100"
    Then vejo a mensagem de transferência concluída

  @caracterizacao
  Scenario Outline: Transferência com valor aceito pelo sistema
    When transfiro "<valor>"
    Then vejo a mensagem de transferência concluída

    Examples:
      | valor |
      | 0     |
      | -50   |

  @caracterizacao
  Scenario: Valor não numérico gera erro interno
    When transfiro "abc"
    Then vejo a mensagem de erro interno

  @caracterizacao
  Scenario: Campo de valor vazio gera erro interno
    When transfiro sem valor
    Then vejo a mensagem de erro interno