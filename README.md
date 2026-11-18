# Automação BDD: ParaBank

Automação de testes BDD para as funcionalidades de **Registro**, **Login** e **Transferência de Fundos** da aplicação de demonstração ParaBank, usando Python, Behave e Playwright.

## Tecnologias

- Python 3.12+
- Behave (BDD, cenários em Gherkin)
- Playwright (automação de navegador)

## Pré-requisitos

- Python 3.12 ou superior
- Git

## Instalação

```powershell
git clone https://github.com/LucasRoMatos/automacao-parabank-bdd.git
cd automacao-parabank-bdd
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Execução

Rodar todos os cenários:

```powershell
python -m behave
```

Rodar uma funcionalidade específica:

```powershell
python -m behave features/registro.feature
python -m behave features/login.feature
```

Rodar apenas os cenários marcados como `@smoke`:

```powershell
python -m behave --tags=@smoke
```

Salvar a saída da execução como evidência:

```powershell
python -m behave > evidencias/execucao.txt
```

## Ambiente alternativo (opcional)

Por padrão, os testes usam o ParaBank público (`https://parabank.parasoft.com/parabank`). Esse site pode exibir um desafio de segurança da Cloudflare de forma intermitente. Para evitar essa interferência, é possível rodar a aplicação localmente com Docker e apontar os testes para ela:

```powershell
docker run -d -p 8080:8080 parasoft/parabank
$env:PARABANK_URL="http://localhost:8080/parabank"
python -m behave
```

## Estrutura do projeto

```
features/      cenários em Gherkin e steps
pages/         Page Objects com seletores e ações
support/       geração de dados de teste
config.py      configuração de ambiente
evidencias/    saídas de execução e screenshots
```

## Cobertura

| Funcionalidade | Cenários |
|---|---|
| Registro | Sucesso, campos obrigatórios, cadastro sem telefone |
| Login | Credenciais válidas, credenciais incorretas, campos vazios |
| Transferência | Saldo suficiente, saldo insuficiente, valor inválido |

## Decisões de projeto

- **Seletores por atributo `name` e `value`**, mais estáveis que classes CSS.
- **Page Object Model**: seletores e ações ficam nas páginas, e os steps só traduzem o Gherkin.
- **Dados únicos a cada execução** no registro, evitando conflito de usuário.
- **Contexto de navegador por cenário**, isolando sessão e cookies entre os testes.
- **URL base em configuração**, para trocar de ambiente sem alterar o código.
- **Cadastro sem telefone**: a tela não exige o campo, então ele é tratado como opcional.

## Limitações conhecidas

- O site público pode exibir o desafio "Confirme que é humano" da Cloudflare. Nesse caso, a suíte informa a causa da falha, e a alternativa é o ambiente local com Docker.