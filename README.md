# Estudos Django 2

Respositório de estudos de Ṕython com Django 2 baseado em:
            
    https://cursos.alura.com.br/course/fundamentos-django-2


# Configurações de ambiente utilizadas (Linux)
 
Ativar venv em deacaplicacao:

```python3 -m venv ./venv```

```source /caminho/completo/ate/o/projeto/deacaplicacao/venv/bin/activate```

Dentro do ambiente virtual (venv) instalar o Django

```pip install django```

*Para sair do ambiente virtual, executar:

```deactivate```


# Iniciar projeto do zero

Dentro da pasta deacaplicacao executar no venv:

```django-admin startproject <nome-d-projeto> .```

# Executar servidor

Dentro da pasta deacaplicacao executar no venv:

```python manage.py runserver```


# Iniciar novo app

Dentro da pasta deacaplicacao executar no venv:

```python manage.py startapp <nome-do-app>```

Adicionar nome do app na chave INSTALLED_APPS em \<nome-do-projeto>/settings.py

# Banco de dados PostgreSQL

Baixar de https://www.postgresql.org/download

Para Linux, após seguir instruções também executar o comando

``` sudo apt-get install pgadmin4```

Abri o PgAdmin e criar uma nova servidor (conexão). Em seguida criar um novo Database. 

Instalar o Pycopg, o adaptador de banco de dados PostgreSQL mais popular para a linguagem de programação Python. No venv executar:

```pip install psycopg2```

```pip install psycopg2-binary```

Adicionar configurações de ENGINE, NAME, USER, PASSWORD e HOST em \<nome-do-projeto>/settings.py

# Django-admin

Adicionar modelos no `admin.py` e acesar a rota pré criada pelo Django `/admin`.

Criar super usuário para acessar área admnistrativa e gerenciar (CRUD) modelos por lá:

```python manage.py createsuperuser```