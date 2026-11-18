Feature: Transferência de fundos

  Background:
    Given que abro a página inicial
    And que existe um usuário cadastrado
    And que acesso a transferência de fundos

  Scenario: Transferência com valor válido
    When transfiro "100"
    Then vejo a mensagem de transferência concluída