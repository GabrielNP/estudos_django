from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from receitas.models import Receita


def cadastro(request):
    """
    Cadastra um novo usuário no sistema
    """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome deve ser corretamente preenchido')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email deve ser corretamente preenchido')
            return redirect('cadastro')

        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário com este e-mail já existe')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def login(request):
    """
    Realiza o login no sistema
    """
    if request.method == 'POST':
        nome = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(nome) or campo_vazio(senha):
            messages.error(request, 'Os campos usuário e senha não podem ficar em branco')
            return redirect('login')

        email = '@' in nome
        if email:
            if User.objects.filter(email=nome).exists():
                nome = User.objects.filter(email=nome).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                if user is not None:
                    auth.login(request, user)
                    print('Usuario logado com sucesso')
        else:
            if User.objects.filter(username=nome).exists():
                user = auth.authenticate(request, username=nome, password=senha)        
                if user is not None:
                        auth.login(request, user)
                        print('Usuario logado com sucesso')

        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


# Validators
def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha1, senha2):
    return senha1 != senha2
