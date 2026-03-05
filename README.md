# 🤖 Automação de Cadastro de Produtos com Python

Automação desenvolvida em Python para cadastrar produtos em massa em um sistema web, eliminando o trabalho manual de preencher formulários campo por campo.

## 📋 Sobre o Projeto

O script lê uma planilha CSV com 293 produtos e cadastra cada um automaticamente no sistema, preenchendo todos os campos do formulário sem nenhuma intervenção humana.

## ⚙️ Funcionalidades

- Abre o navegador e acessa o sistema automaticamente
- Realiza login com as credenciais configuradas
- Lê os dados diretamente de uma planilha `.csv`
- Preenche os campos: código, marca, tipo, categoria, preço unitário, custo e observações
- Trata campos vazios (`NaN`) sem quebrar a execução
- Cadastra todos os produtos em sequência

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — automação de interface
- [Pandas](https://pandas.pydata.org/) — leitura e manipulação de dados

## 📁 Estrutura do Projeto

```
📦 automacao-cadastro-produtos
 ┣ 📄 codigo.py        # Script principal
 ┣ 📄 produtos.csv     # Base de dados dos produtos
 ┗ 📄 README.md
```

## ▶️ Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

**2. Instale as dependências**
```bash
pip install pyautogui pandas
```

**3. Configure suas credenciais**

No arquivo `codigo.py`, altere os campos de login:
```python
pyautogui.write("seu-email@gmail.com")
pyautogui.write("sua-senha")
```

**4. Execute o script**
```bash
python codigo.py
```

> ⚠️ **Atenção:** Não mova o mouse para os cantos da tela durante a execução. O PyAutoGUI possui um mecanismo de segurança (failsafe) que interrompe o programa caso isso aconteça.
> 
> ⚠️ **Atenção:** Talvez seja necessário adaptação nas coordenadas para funcionar no seu PC.


## 📊 Estrutura da Planilha

O arquivo `produtos.csv` deve conter as seguintes colunas:

| Coluna | Descrição |
|---|---|
| `codigo` | Código único do produto |
| `marca` | Marca do produto |
| `tipo` | Tipo/categoria do produto |
| `categoria` | Número da categoria |
| `preco_unitario` | Preço de venda |
| `custo` | Custo do produto |
| `obs` | Observações (opcional) |

## 💡 Por que não usar um agente de IA?

Agentes de IA brilham em problemas complexos — tomada de decisão, linguagem natural, contexto variável. Aqui o problema é simples e repetitivo: a ferramenta certa para o problema certo.

Sem custo de API. Sem infraestrutura extra. Sem respostas inesperadas. Só Python rodando e o trabalho sendo feito.

## 👨‍💻 Autor

Feito por **Kauã Kley** — projeto desenvolvido durante estudos de automação e análise de dados com Python.
