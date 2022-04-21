from django.shortcuts import redirect, render, get_object_or_404
from . forms import LoginForm, RegisterForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'index.html'

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                         password=password)
        
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                
                else:
                    messages.info(request, 'Disabled Account')
            else:
                 messages.info(request, 'Check Your Username and Password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

        
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('index')


