from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST' :
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(request, username=username, password=password) # 실제 저장된 username과 passsword 인지 확인
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

def signup(request):
    return 



