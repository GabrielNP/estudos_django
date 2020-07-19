# Estudos Django 2

Respositório de estudos de Ṕython com Django 2 baseado em:
            
    https://cursos.alura.com.br/course/fundamentos-django-2


# Configurações de ambiente utilizadas (Linux)
 
Ativar venv em introducao/aplicacao:

```python3 -m venv ./venv```

```source /caminho/completo/ate/o/projeto/introducao/aplicacao/venv/bin/activate```

Dentro do ambiente virtual (venv) instalar o Django

```pip install django```

*Para sair do ambiente virtual, executar:

```deactivate```


# Iniciar projeto do zero

Dentro da pasta introducao/aplicacao executar no venv:

```django-admin startproject <nome-d-projeto> .```

# Executar servidor

Dentro da pasta introducao/aplicacao executar no venv:

```python manage.py runserver```


# Iniciar novo app

Dentro da pasta introducao/aplicacao executar no venv:

```python manage.py startapp <nome-do-app>```

Adicionar nome do app na chave INSTALLED_APPS em \<nome-do-projeto>/settings.py