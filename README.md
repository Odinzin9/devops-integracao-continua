# DevOps Task API

API REST desenvolvida como parte da atividade prática das disciplinas de **DevOps e Integração Contínua** (UNINTER), simulando uma solução de consultoria para a empresa fictícia **CodeFactory Solutions**, aplicando práticas de versionamento, containerização e integração contínua.

## Objetivo

Demonstrar, na prática, como a Cultura DevOps pode transformar o fluxo de desenvolvimento de uma equipe, utilizando controle de versão com Git/GitHub, containerização com Docker e automação de pipeline com GitHub Actions.

## Tecnologias utilizadas

- **Python 3.12**
- **FastAPI** — framework web para construção da API
- **Uvicorn** — servidor ASGI
- **Pydantic** — validação de dados
- **Pytest / HTTPX** — testes automatizados
- **Docker** — containerização da aplicação
- **GitHub Actions** — pipeline de Integração Contínua

## Estrutura de pastas

devops-integracao-continua/
├── app/
│ ├── init.py
│ └── main.py
├── tests/
│ └── test_api.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md


## Instruções de instalação

```bash
git clone https://github.com/Odinzin9/devops-integracao-continua.git
cd devops-integracao-continua
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Instruções de execução

### Local

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa em `http://127.0.0.1:8000/docs`.

### Via Docker

```bash
docker build -t devops-task-api .
docker run -d -p 8000:8000 --name devops-task-api devops-task-api
```

## Rodando os testes

```bash
pytest -v
```

## Por que utilizar container neste projeto?

O uso de Docker elimina o problema de "na minha máquina funciona": qualquer novo integrante da equipe consegue subir o ambiente completo com um único comando, sem precisar configurar Python, dependências ou versões manualmente. Isso reduz o tempo de onboarding e garante consistência entre ambiente de desenvolvimento, testes e produção.

## Licença

Este projeto está licenciado sob a licença MIT.