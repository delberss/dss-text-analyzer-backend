# 🎬 Text Analyzer - Backend

<p align="center">
  <a href="https://dss-text-analyzer-frontend.vercel.app/" target="_blank">
    <img src="./docs/banner-readme.png" alt="Preview" width="600" />
  </a>
</p>


> Plataforma que recebe um texto e faz a análise da quantidade de letras, palavras, frases, linhas, média de palavras por frase, etc. Utilizando **Python**, **FastAPI**, **Starlette**, **Uvicorn** e **python-multipart** para processamento das requisições.

🔗 **Acesse online:** [https://dss-text-analyzer-frontend.vercel.app/](https://dss-text-analyzer-frontend.vercel.app/)

---

## 🚀 Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

- 🐍 **Python**
- ⚡ [FastAPI](https://fastapi.tiangolo.com/) — framework moderno e rápido para APIs
- 🌐 [Starlette](https://www.starlette.io/) — base assíncrona utilizada pelo FastAPI
- 🚀 [Uvicorn](https://www.uvicorn.org/) — servidor ASGI de alta performance
- 📩 [python-multipart](https://andrew-d.github.io/python-multipart/) — para processamento de formulários e uploads


---
## 📁 Estrutura do Projeto
```
dss-text-analyzer-backend/
│
├── docs/
│   └── ... # Imagens e arquivos usados no README
│
├── __pycache__/
│   └── ... # Arquivos cache do Python
│
├── venv/
│   └── ... # Ambiente virtual (não é versionado no GitHub)
│
├── main.py            # Arquivo principal da aplicação FastAPI
├── run.py             # Script para iniciar o servidor localmente
├── requirements.txt   # Dependências do projeto
├── .gitignore         # Arquivos e pastas ignorados pelo Git
└── README.md          # Documentação do projeto

```

---

## ⚛️ Projeto FRONTEND

https://github.com/delberss/dss-text-analyzer-frontend


## 🖥️ Como Rodar Localmente

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/delberss/dss-text-analyzer-backend
```
### 2️⃣ Acesse a pasta do projeto
```bash
cd dss-text-analyzer-backend
```
### 3️⃣ Crie o ambiente virtual

```bash
python3 -m venv venv
```
### 4️⃣ Ative o ambiente virtual - Windows (PowerShell ou CMD)
```bash
venv\Scripts\activate
```
### 4️⃣ Ative o ambiente virtual - Windows (Git Bash) / Linux / macOS
```bash
source venv/Scripts/activate
```
### 5️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```
### 6️⃣ Execute o servidor FastAPI
```bash
python run.py
```
### 7️⃣ Acesse no navegador
```bash
http://localhost:8000/health
```