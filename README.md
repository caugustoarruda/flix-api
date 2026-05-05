
# **`Documentação do projeto Flix-api`**

# Funcionalidades do projeto
- `Funcionalidade 1`: Gerenciamento de Flix | CRUD completo
- `Funcionalidade 2`: Gerenciamento de Acessos, criação e acesso com login

<!-- # 📁 Acesso ao projeto
**Indique como é possível baixar ou acessar o código fonte do projeto, seja projeto inicial ou final** -->

# 🛠️ Abrir e rodar o projeto
**Instruções necessárias executar o projeto**

#### Partindo do pressuposto que já tenha o Python instalado e um terminal para executar os comandos
1. Clone the repo  
```bash 
git clone https://github.com/caugustoarruda/flix-api 
```
2. Ative ou Crie seu ambiente virtual
```bash 
python -m venv env ou source/bin/activate para ativar um ambiente virtual ja existente
```
3. Instale as dependencias  
```bash 
pip install -r requirements.txt
```
4. Tenha um gerenciador de banco de dados instalado ou utilize o sqlite, banco padrão adotado pelo Django

5. O próximo passo será definir qual sera o banco de dados utilizado, alterando uma simples configuração no `settings` do projeto 

   - vá na pasta app do projeto e procure por `settings.py`
   - procure onde está a definição de banco de dados `DATABASES`
   - e ai agora é so configurar com seu banco preferido seguindo os exemplos abaixo:

   sqlite
   ```py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
   ```
   postgres
   ```py
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'NOME DO SEU BANCO',
          'USER': 'USUARIO DO BANCO',
          'PASSWORD': 'SENHA',
          'HOST': 'localhost',
          'PORT': '5432'
      }
    }
   ```
6. Seguindo, será necessário executar o comando migrate do Django, para que seja criado as tabelas necessárias para que a aplicação rode
```py
   python manage.py migrate
```
7. Se chegou até aqui, agora é so executar o comando para disponibilizar o projeto localmente
```py
   python manage.py runserver
```

Como esse projeto se trada de uma api, dada a criação do superuser, esse usuário terá acesso a todos os endpoints, mas para isso tera que se logar receber seu access token, e em cada chamada utilizar o Bearer Token e informar o access token gerado
   - 127.0.0.1:8000/api/v1/authentication/token/ - informe no body informe o paylod username e password
   ```py
     {
      'username': 'flixapp',
      'password': 'suasenha'
    }
   ```
   Voce irá receber o retorno abaixo, se autenticou com sucesso
   ```py
     {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.          eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3ODA3NjE0OSwiaWF0IjoxNzc3OTg5NzQ5LCJqdGkiOiI0NjM2NDMzNmU4YjA0ODkyYjk4ZTZmNTYwYjljMDI2OCIsInVzZXJfaWQiOiIyIn0.CQv7FC9a7WVASI8D4z2khUQgur1e1SZV1pxzG3F0U6k",
        
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3OTkwMDQ5LCJpYXQiOjE3Nzc5ODk3NDksImp0aSI6IjZiZTcyMjk1MGI4ZDQzMDVhOGQyNjNmNGJlOWVjMGRkIiwidXNlcl9pZCI6IjIifQ.LIv-bpSwkIrL_dQAY1AZjIIeCbMbRELx0AINxfLxgAk"
    }
   ```