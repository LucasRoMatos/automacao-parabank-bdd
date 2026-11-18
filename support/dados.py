import time


def novo_usuario():
    sufixo = int(time.time())
    return {
        "primeiro_nome": "Lucas",
        "ultimo_nome": "Teste",
        "endereco": "Rua das Flores, 100",
        "cidade": "Mogi das Cruzes",
        "estado": "SP",
        "cep": "08700000",
        "telefone": "11999999999",
        "ssn": "123456789",
        "usuario": f"usuario{sufixo}",
        "senha": "Senha@123",
        "confirma_senha": "Senha@123",
    }