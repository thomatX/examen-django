from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout, login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Usuario

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    username = request.user.username
    usuario = Usuario.objects.get(email=username)
    print(str(usuario.name))
    return render(request,'index.html',{'nombre':usuario.name})

def lists(request):
    return render(request,'lists.html')

def products(request):
    return render(request,'products.html')

def shopping(request):
    return render(request,'shopping.html')

def profile(request):
    return render(request,'profile.html')


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def create_user(request):
    try:
        email = request.POST.get('email')
        print(email)
        name = request.POST.get('name')
        print(name)
        password = request.POST.get('pass')
        print(password)
        age = request.POST.get('age')
        print(age)
        userAuth = User.objects.create_user(email, email=email, password=password)
        userAuth.save()
        user = Usuario(email=email, name=name, password=password, age=age)
        user.save()
        return HttpResponse('<script>alert("Usuario registrado correctamente!"); window.location.href="/login/";</script>')
    except Exception as ex:
        print(str(ex))
        return HttpResponse('<script>alert("Se ha ingresado un valor incorrecto... Intenta nuevamente."); window.location.href="/register/";</script>')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto."); window.location.href="/login/";</script>')

def login_iniciar(request):
    usuario = request.POST.get('email','')
    print(usuario)
    contrasenia = request.POST.get('pass','')
    print(contrasenia)
    user = authenticate(request,username=usuario, password=contrasenia)
    print(user)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/login/";</script>')
