# Conexão Viva -
 É um aplicativo voltado para ajudar pessoas com depressão por meio de mensagens de apoio, diário emocional e ferramentas de emergência. Além disso, o projeto visa promover bem-estar e facilitar o acesso à ajuda de forma acessível, discreta e eficiente.

**Conexão Viva** é um aplicativo fullstack multiplataforma voltado para o apoio emocional de pessoas em situação de vulnerabilidade. O sistema integra backend com FastAPI e frontend com React, utilizando Docker e Docker Compose para orquestração. Além de demonstrar uma arquitetura moderna e escalável, o projeto também disponibiliza funcionalidades essenciais voltadas à saúde mental.

## 🎯 Objetivo

Demonstrar a integração entre frontend (React) e backend (FastAPI), oferecendo uma aplicação web moderna com API REST, contêineres Docker e uma interface responsiva. Além disso, o projeto serve como uma ferramenta de suporte emocional por meio de funcionalidades práticas e acessíveis.

---

## ⚙️ Funcionalidades

### Funcionalidades do Aplicativo Conexão Viva

- ✅ Envio de mensagens positivas automáticas
- ✅ Página de socorro imediato com informações rápidas de ajuda
- ✅ Diário emocional para registro de sentimentos
- ✅ Área do usuário para personalização da experiência
- ✅ Informações úteis sobre saúde mental
- ✅ Páginas institucionais: Sobre, Contato, Termos e Privacidade

### Funcionalidades Técnicas

- ✅ Backend com API REST usando FastAPI (rota `/api`)
- ✅ Frontend React que consome dados da API
- ✅ Deploy e execução com Docker + Docker Compose
- ✅ Arquitetura preparada para multiplataforma e CI/CD

---

## 🧱 Arquitetura e Tecnologias Utilizadas

- **Backend**: FastAPI + Python
- **Frontend**: React.js + NGINX
- **Orquestração**: Docker Compose
- **Comunicação**: API REST via `fetch()`
- **Rede Docker**: Comunicação interna entre containers

---

## 📁 Estrutura de Diretórios

```
conexaoviva/
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── models.py
│   ├── database.py
│   ├── requirements.txt
│   ├── Dockerfile
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── Dockerfile
├── docker-compose.yml
├── README.md
```

---

## 🚀 Execução do Projeto

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Instruções

1. Clone o repositório:
```bash
git clone https://github.com/MaryaJoSo/conexao-viva.git
cd conexaoviva
```

2. Execute com Docker Compose:
```bash
docker-compose up --build
```

3. Acesse no navegador:
- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend (Swagger Docs): [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧩 Multiplataforma

| Plataforma     | Suporte                           |
|----------------|------------------------------------|
| Linux/macOS    | Docker roda nativamente            |
| Windows        | Compatível com Docker Desktop      |
| Nuvem          | Deploy fácil em AWS, Azure, GCP    |
| CI/CD          | Pronto para integração contínua    |

---

## 👨‍💻 Equipe

- Karine Duarte
- Maria Sousa
- Mateeus Camurca
- Francisco Matheus
- Cleany Teixeira
- Professor colaborador: `profmiqueias`

---

## 📜 Licença

Este projeto está licenciado sob os termos da licença MIT.
