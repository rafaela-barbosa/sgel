# 📚 Sistema de Gerenciamento de Empréstimos de Livros

Este projeto consiste em um sistema de backend desenvolvido em **Django** para o controle de acervos e gestão de empréstimos bibliotecários.  

O foco principal é a utilização do **Django Admin** como interface de gerenciamento, demonstrando a eficiência do framework na criação de aplicações robustas com baixo esforço de interface manual.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python  
- **Framework Web:** Django  
- **Banco de Dados:** SQLite (padrão de desenvolvimento) ou PostgreSQL  
- **Interface:** Django Administration (Contrib App)

---

## 🚀 Como Executar

### Pré-requisitos
- [Docker](https://www.docker.com/products/docker-desktop/) instalado e rodando

### Passo a passo

1. Clone o repositório:
```bash
   git clone https://github.com/rafaela-barbosa/sgel.git
```

2. Crie o arquivo `.env` dentro da pasta `backend/` seguindo o modelo do `.env.example`

3. Suba os containers:
```bash
   docker compose up --build
```

4. Em outro terminal, rode as migrações:
```bash
   docker compose exec web python manage.py migrate
```

5. (Opcional) Crie um superusuário para acessar o Django Admin:
```bash
   docker compose exec web python manage.py createsuperuser
```

Acesse o sistema em: http://localhost:8000
Django Admin em: http://localhost:8000/admin
