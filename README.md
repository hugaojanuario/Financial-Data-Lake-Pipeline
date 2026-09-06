# Financial Data Lake Pipeline

Projeto autoral de portfólio desenvolvido para aplicar conceitos de Engenharia de Dados em um cenário financeiro.

O objetivo é construir, de forma incremental, um pipeline capaz de coletar dados públicos do mercado financeiro, armazenar o conteúdo bruto, tratar e validar os dados e disponibilizá-los para consultas analíticas na AWS.

> Este projeto possui finalidade exclusivamente educacional e não representa recomendação de investimento.

## Estado atual

O projeto está em desenvolvimento. Atualmente, realiza:

- Consulta de cotações de ações brasileiras pela API da brapi;
- Tratamento de timeout e erros HTTP;
- Armazenamento da resposta original em JSON;
- Organização dos arquivos por ativo e data da coleta;
- Identificação do horário e fuso da execução no nome do arquivo.

Exemplo de organização dos dados:

```text
data/raw/stocks/PETR4/2026/09/05/20260905T234830-0300.json
```

## Tecnologias

- Python
- API REST
- JSON
- AWS (planejado)

## Estrutura atual

```text
.
├── data/
│   └── raw/
│       └── stocks/
├── src/
│   └── ingestion/
│       └── extract_stock.py
└── README.md
```

## Executando localmente

Pré-requisitos:

- Python 3.9 ou superior;
- Biblioteca `requests`.

Instale a dependência:

```bash
python3 -m pip install requests
```

Execute a extração:

```bash
python3 src/ingestion/extract_stock.py
```

## Próximas etapas

- Coletar múltiplos ativos em uma mesma execução;
- Criar testes automatizados;
- Implementar logs estruturados;
- Enviar os dados brutos para o Amazon S3;
- Converter os dados para Parquet;
- Catalogar os dados com AWS Glue;
- Consultar os dados com Amazon Athena;
- Adicionar validações de qualidade e observabilidade;
- Automatizar a infraestrutura com Terraform.

## Fonte dos dados

- [brapi](https://brapi.dev/): dados do mercado financeiro brasileiro.

Os dados pertencem aos seus respectivos provedores e estão sujeitos aos termos de uso de cada fonte.
