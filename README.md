# Estudos Django 2

Respositório de estudos de Python com Django 2 baseado em:
            
- https://cursos.alura.com.br/course/fundamentos-django-2

- https://cursos.alura.com.br/course/integracao-modelos-django-2

- https://cursos.alura.com.br/course/autenticacao-django-2

- https://cursos.alura.com.br/course/django-2-boas-praticas

# Dependências
- Python 3
- PostgreSQL

# Configurações de ambiente

*Configurações relizadas em sistema operacional Linux.

## Clonar projeto

```
git clone https://github.com/GabrielNP/estudos_django.git
```

## Criar ambiente virtual do Python (venv)
```
// Criar
python3 -m venv .venv

// Ativar
source /caminho/completo/ate/o/projeto/aplicacao/.venv/bin/activate
```

## Instalar bibliotecas necessárias
```
// Com o ambiente virtual ativado e dentro do diretório aplicacao
pip install -r requirements.txt
```

*Para sair do ambiente virtual basta executar:

```
deactivate
```

## Banco de dados
1. Baixar de https://www.postgresql.org/download

2. Para Linux após seguir instruções também executar o comando

    ``` 
    sudo apt-get install pgadmin4
    ```

3. Abrir o PgAdmin e criar um nova conexão. Em seguida criar um novo Database.

4. Adicionar configurações de ENGINE, NAME, USER, PASSWORD e HOST em `aplicacao/aluraceita/settings.py`

## Executar as migrações
```
// Em aplicacao
python manage.py migrate
```
# Como executar
 
1. Ativar ambiente virtual (venv)
2. Executar servidor

    Dentro da pasta de acaplicacao executar no venv:

    ```
    python manage.py runserver
    ```
# Doc Django
## Iniciar projeto do zero

Dentro da pasta deacaplicacao executar no venv:

```
django-admin startproject <nome-d-projeto> .
```

## Iniciar novo app

Dentro da pasta deacaplicacao executar no venv:

```
python manage.py startapp <nome-do-app>
```

Adicionar nome do app na chave INSTALLED_APPS em \<nome-do-projeto>/settings.py

## Django-admin

Adicionar modelos no `admin.py` e acesar a rota pré criada pelo Django `/admin`.

Criar super usuário para acessar área admnistrativa e gerenciar (CRUD) modelos por lá:

```
python manage.py createsuperuser
```
## Banco de dados PostgreSQL

Baixar de https://www.postgresql.org/download

Para Linux, após seguir instruções também executar o comando

``` sudo apt-get install pgadmin4```

Abrir o PgAdmin e criar uma nova servidor (conexão). Em seguida criar um novo Database. 

Instalar o Pycopg, o adaptador de banco de dados PostgreSQL mais popular para a linguagem de programação Python. No venv executar:

```pip install psycopg2```

```pip install psycopg2-binary```

Adicionar configurações de ENGINE, NAME, USER, PASSWORD e HOST em \<nome-do-projeto>/settings.py


