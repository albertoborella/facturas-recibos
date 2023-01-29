from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'usuarios/home.html')

# @login_required()
# def libros(request):
#     return render(request, 'main/libros.html')

def register(request):
    data = { 'form': CustomUserCreationForm() }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()

            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)

            return redirect('home')

    return render(request, 'registration/register.html', data)

def salir(request):
    logout(request)
    return redirect('home')
