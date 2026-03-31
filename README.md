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

Para rodar o projeto localmente, siga os passos abaixo:

### 1. Clone o repositório
  ```bash
  git clone https://github.com/seu-usuario/nome-do-projeto.git
```
2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure as variáveis do ambiente:**
   Crie um arquivo .env na raiz do projeto seguindo o modelo do .env.example
5. **Rode as migrações do banco de dados:**
   ```bash
   python manage.py migrate
6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
  Acesse o sistema em: http://127.0.0.1:8000/admin
