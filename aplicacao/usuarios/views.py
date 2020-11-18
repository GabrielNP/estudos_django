from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['pasword']
        senha2 = request.POST['pasword2']

        if not nome.strip():
            print('O campo nome deve ser corretamente preenchido')
            return redirect('cadastro')

        if not email.strip():
            print('O campo email deve ser corretamente preenchido')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas não são iguais')

        if User.objects.filter(email=email).exists():
            print('Usuário com este e-mail já existe')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        print(f'Dados do cadastro\nNome: {nome}\nE-mail: {email}\nSenha: {senha}')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['pasword']

        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Usuario logado com sucesso')

        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')