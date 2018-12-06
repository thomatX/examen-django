from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout, login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Usuario, Lista, Producto
from random import randint

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    username = request.user.username
    usuario = Usuario.objects.get(email=username)
    print(str(usuario.name))
    return render(request,'index.html',{'nombre':usuario.name})

def lists(request):
    email = request.user.username
    lists = Lista.objects.filter(email=email)
    for x in lists:
        print(str(x))
    return render(request,'lists.html',{'lists':lists})

def create_list(request):
    return render(request,'create_list.html')

def create_product(request):
    return render(request,'create_product.html')

def products(request):
    email = request.user.username
    products = Producto.objects.filter(email=email)
    for x in products:
        print(str(x))
    return render(request,'products.html',{'products':products})

def shopping(request):
    products = Producto.objects.all()
    for x in products:
        print(str(products))
    return render(request,'shopping.html',{'products':products})

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

def create_new_list(request):
    try:
        id_pk = randint(0,9999999)
        print(str(id_pk))
        total_productos = 0
        total_productos_comprados = 0
        total_real = 0
        email = request.user.username
        print(email)
        name = request.POST.get('name')
        print(name)
        presupuestado = request.POST.get('presupuestado')
        print(presupuestado)
        lista = Lista(id_pk = id_pk, email = email, name = name, total_productos = total_productos, total_productos_comprados = total_productos_comprados, total_presupuestado = presupuestado, total_real = total_real)
        lista.save()
        return HttpResponse('<script>alert("Tu lista ha sido añadida correctamente!"); window.location.href="/lists/";</script>')
    except Exception as ex:
        print("Error: "+str(ex))
        return HttpResponse('<script>alert("Ha ocurrido un error, intenta nuevamente!"); window.location.href="/lists/create/";</script>')

def create_new_product(request):
    try:
        id_pk = randint(0,9999999)
        print(str(id_pk))
        name = request.POST.get('name')
        print(name)
        description = request.POST.get('description')
        print(description)
        price = request.POST.get('price')
        print(price)
        email = request.user.username
        print(email)
        product = Producto(id_pk = id_pk,name = name, description = description, price = price, email = email)
        product.save()
        return HttpResponse('<script>alert("Tu producto ha sido añadido correctamente!"); window.location.href="/products/";</script>')
    except Exception as ex:
        print("Error: "+str(ex))
        return HttpResponse('<script>alert("Ha ocurrido un error, intenta nuevamente!"); window.location.href="/products/create/";</script>')



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
