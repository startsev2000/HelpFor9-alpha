from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):  #регистрация пользователя
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 
        email = request.POST['email']

        if password1 == password2: 

            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'Пользователь с таким именем уже существует')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Пользователь с электронной почтой уже существует')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('Пользователь создан')
                
        else:
            messages.info(request, 'Пароли не совпадают')
            return redirect('register')

        return redirect('login')

    else:
        return render(request, 'register.html')

def login(request): #форма для входа пользователя в систему
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Пользователь не существует')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request): #выйти из аккаунта
    auth.logout(request)
    return redirect('/')
