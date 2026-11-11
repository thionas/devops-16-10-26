# 📋 API Lista de Tarefas — Práticas de DevOps

Aplicação desenvolvida para o módulo de **Extensão em DevOps**, com foco na implementação de esteiras automatizadas de **Integração Contínua (CI)** e **Entrega Contínua (CD)**, conteinerização e implantação em nuvem. O projeto oferece suporte integral a desenvolvimento em nuvem via **GitHub Codespaces**.

---

## 📌 Sumário
- [Sobre a Aplicação](#-sobre-a-aplicação)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instruções para Execução Local](#-instruções-para-execução-local)
  - [1. Clonar o Repositório](#1-clonar-o-repositório)
  - [2. Inicializar o Banco de Dados (PostgreSQL via Docker)](#2-inicializar-o-banco-de-dados-postgresql-via-docker)
  - [3. Configurar e Executar a API](#3-configurar-e-executar-a-api)
- [Documentação da API (Swagger UI)](#-documentação-da-api-swagger-ui)
- [Implantação em Produção (Render)](#-implantação-em-produção-render)
- [Qualidade de Código e Testes](#-qualidade-de-código-e-testes)
- [Pipeline de CI/CD](#-pipeline-de-cicd)

---

## 📖 Sobre a Aplicação

A API REST disponibiliza operações completas de CRUD (Criação, Leitura, Atualização e Exclusão) para gerenciamento de listas de tarefas. Foi construída visando alto desempenho, tipagem estrita com Pydantic/SQLModel, persistência relacional em PostgreSQL e orquestração de contêineres para ambientes locais e escaláveis.

---

## 🛠 Tecnologias Utilizadas

| Categoria | Tecnologias |
| :--- | :--- |
| **Framework & API** | [FastAPI](https://fastapi.tiangolo.com/), [HTTPX](https://www.python-httpx.org/) |
| **ORM & Banco de Dados** | [SQLModel](https://sqlmodel.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [PostgreSQL](https://www.postgresql.org/), `psycopg[binary]`, `PyMySQL` |
| **Testes Automatizados** | [Pytest](https://docs.pytest.org/), [pytest-cov](https://pytest-cov.readthedocs.io/) |
| **Qualidade & Segurança** | [Ruff](https://docs.astral.sh/ruff/), [Pylint](https://pylint.org/), [Bandit](https://bandit.readthedocs.io/) (Security Linter) |
| **Containers & Orquestração** | [Docker](https://www.docker.com/), [Minikube](https://minikube.sigs.k8s.io/), [Kubernetes](https://kubernetes.io/) |
| **CI/CD & Cloud** | [GitHub Actions](https://github.com/features/actions), [GitHub Codespaces](https://github.com/features/codespaces), [Render](https://render.com/) |

---

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:
- [Git](https://git-scm.com/)
- [Python 3.10+](https://www.python.org/)
- [Docker](https://docs.docker.com/get-docker/)

---

## 🚀 Instruções para Execução Local

### 1. Clonar o Repositório

Clone o projeto para o seu ambiente local ou abra diretamente no **GitHub Codespaces**:

```bash
git clone https://github.com/thionas/devops-16-10-26.git
cd devops-16-10-26
```

### 2. Inicializar o Banco de Dados (PostgreSQL via Docker)

Inicie um contêiner Docker rodando a instância do banco de dados relacional PostgreSQL:

```bash
docker run -d \
  --name postgres-devops \
  -e POSTGRES_USER=devops \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=devops \
  -p 5432:5432 \
  postgres
```

### 3. Configurar e Executar a API

#### A. Criar e Ativar o Ambiente Virtual (Opcional, porém recomendado)

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

#### B. Iniciar a Aplicação com Variáveis de Ambiente

Execute o servidor passando as credenciais de conexão do banco de dados:

```bash
# Linux / macOS / Codespaces (Bash)
DATABASE_ADDRESS=localhost \
DATABASE_PASSWORD=password \
DATABASE=devops \
DATABASE_USERNAME=devops \
fastapi run
```

```powershell
# Windows (PowerShell)
$env:DATABASE_ADDRESS="localhost"
$env:DATABASE_PASSWORD="password"
$env:DATABASE="devops"
$env:DATABASE_USERNAME="devops"
fastapi run
```

> **Nota:** Caso utilize o comando padrão do Uvicorn, execute:  
> `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

---

## 📚 Documentação da API (Swagger UI)

Com a aplicação em execução, acesse a documentação interativa gerada automaticamente pelo FastAPI:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## ☁️ Implantação em Produção (Render)

A aplicação está configurada para deploy automático na nuvem através do **Render**:

1. A imagem Docker é construída e publicada automaticamente a cada alteração aprovada.
2. O serviço no Render é atualizado continuamente.
3. Para consultar os endpoints em produção, acesse a URL fornecida pelo serviço acrescida da rota de documentação:
   * **Swagger em Produção:** `https://<sua-aplicacao>.onrender.com/docs`

---

## 🧪 Qualidade de Código e Testes

Para garantir a confiabilidade e aderência às boas práticas, utilize os comandos abaixo:

```bash
# Executar suíte de testes com relatório de cobertura
pytest --cov=. -v

# Análise estática e formatação de código (Ruff e Pylint)
ruff check .
pylint main.py

# Verificação de segurança de código estático (Bandit)
bandit -r .
```

---

## 🔄 Pipeline de CI/CD

O ciclo de vida de desenvolvimento é automatizado via **GitHub Actions**:

* **Integração Contínua (CI):** Disparada em todo *Pull Request* direcionado à branch `main`, validando testes unitários e qualidade do código (*linters*).
* **Entrega Contínua (CD):** Disparada após o *merge* na branch `main`, gerando e publicando a nova imagem Docker no registry e sincronizando com o ambiente do **Render**.

---

## 👤 Autor

* **Desenvolvido por:** [Thionas / @thionas](https://github.com/thionas)
* **Repositório:** [devops-16-10-26](https://github.com/thionas/devops-16-10-26)
