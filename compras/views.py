from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout, login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Usuario, Lista, Producto, ProductoCliente, Tienda
from random import randint

#rest_framework
from rest_framework import generics
from .serializers import UsuarioSerializer, ListaSerializer, ProductoSerializer, ProductoClienteSerializer, TiendaSerializer

#rest_framework views

class UsuarioList(generics.ListCreateAPIView):
    try:
        queryset = Usuario.objects.all()
        serializer_class = UsuarioSerializer

        def get_object(self):
            queryset = self.get_queryset
            obj = get_object_or_404(
                queryset,
                pk=self.kwargs['pk'],
            )
            return obj
    except TypeError as ex:
        print("Error: "+str(ex))

class ListaList(generics.ListCreateAPIView):
    try:
        queryset = Lista.objects.all()
        serializer_class = ListaSerializer

        def get_object(self):
            queryset = self.get_queryset
            obj = get_object_or_404(
                queryset,
                pk=self.kwargs['pk'],
            )
            return obj
    except TypeError as ex:
        print("Error: "+str(ex))

class ProductoList(generics.ListCreateAPIView):
    try:
        queryset = Producto.objects.all()
        serializer_class = ProductoSerializer

        def get_object(self):
            queryset = self.get_queryset
            obj = get_object_or_404(
                queryset,
                pk=self.kwargs['pk'],
            )
            return obj
    except TypeError as ex:
        print("Error: "+str(ex))

class TiendaList(generics.ListCreateAPIView):
    try:
        queryset = Tienda.objects.all()
        serializer_class = TiendaSerializer

        def get_object(self):
            queryset = self.get_queryset
            obj = get_object_or_404(
                queryset,
                pk=self.kwargs['pk'],
            )
            return obj
    except TypeError as ex:
        print("Error: "+str(ex))

class ProductoClienteList(generics.ListCreateAPIView):
    try:
        queryset = ProductoCliente.objects.all()
        serializer_class = ProductoClienteSerializer

        def get_object(self):
            queryset = self.get_queryset
            obj = get_object_or_404(
                queryset,
                pk=self.kwargs['pk'],
            )
            return obj
    except TypeError as ex:
        print("Error: "+str(ex))

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    return render(request,'index.html')

@login_required(login_url='/login/')
def lists(request):
    email = request.user.username
    lists = Lista.objects.filter(email=email)
    for x in lists:
        print(str(x))
    return render(request,'lists.html',{'lists':lists})

@login_required(login_url='/login/')
def create_list(request):
    return render(request,'create_list.html')

@login_required(login_url='/login/')
def create_product(request):
    return render(request,'create_product.html')

@login_required(login_url='/login/')
def create_shop(request):
    return render(request,'create_shop.html')

@login_required(login_url='/login/')
def products(request):
    email = request.user.username
    products = Producto.objects.filter(email=email)
    tienda = Tienda.objects.all().filter(email=email)
    print("Tienda: "+str(tienda))
    for x in products:
        print(str(x))
    return render(request,'products.html',{
        'products':products,
        'tienda':tienda
        })

@login_required(login_url='/login/')
def shopping(request):
    products = Producto.objects.all()
    for x in products:
        print(str(products))
    return render(request,'shopping.html',{'products':products})


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

@login_required(login_url='/login/')
def create_new_shop(request):
    try:
        id_pk = randint(0,9999999)
        name = request.POST.get('name')
        sucursal = request.POST.get('sucursal')
        adress = request.POST.get('adress')
        city = request.POST.get('city')
        region = request.POST.get('region')
        email = request.user.username
        shop = Tienda(id_pk=id_pk, email=email, name=name, nombre_sucursal=sucursal,direccion=adress,ciudad=city,region=region)
        shop.save()
        return HttpResponse('<script>alert("Tienda creada correctamente!"); window.location.href="/products/";</script>')
    except Exception as ex:
        print(str(ex))
        return HttpResponse('<script>alert("Se ha ingresado un valor incorrecto... Intenta nuevamente."); window.location.href="/shops/create/";</script>')



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

@login_required(login_url='/login/')
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
        image = request.FILES.get('product-image','no-image')
        print(image)
        product = Producto(id_pk = id_pk,name = name, description = description, price = price, email = email, image=image)
        product.save()
        return HttpResponse('<script>alert("Tu producto ha sido añadido correctamente!"); window.location.href="/products/";</script>')
    except Exception as ex:
        print("Error: "+str(ex))
        return HttpResponse('<script>alert("Ha ocurrido un error, intenta nuevamente!"); window.location.href="/products/create/";</script>')


@login_required(login_url='/login/')
def delete_product(request, pk, template_name='products_confirm_delete.html'):
    product = get_object_or_404(Producto, pk=pk)    
    if request.method=='POST':
        product.delete()
        return redirect('/products/')
    return render(request, template_name, {'object':product})

@login_required(login_url='/login/')
def products_add_list(request, pk, template_name='products_confirm_add.html'):
    try:
        product = get_object_or_404(Producto, pk=pk)
        id_producto_cliente = randint(0,9999999)
        lista = request.POST.get('pick_list')
        print(str(lista))
        lista = Lista.objects.filter(name=lista)
        print(str(lista))
        id_lista = lista.id_pk
        print(str(id_lista))
        id_producto = product.id_pk

        if request.method=='POST':
            list_product = ProductoCliente(id_producto_cliente=id_producto_cliente,id_lista=id_lista,id_producto=id_producto)
            list_product.save()
            return redirect('/lists/')
        return render(request, template_name, {'object':product})
    except Exception as ex:
        print("Error: "+str(ex))
        return False

@login_required(login_url='/login/')
def delete_list(request, pk, template_name='lists_confirm_delete.html'):
    lista = get_object_or_404(Lista, pk=pk)    
    if request.method=='POST':
        lista.delete()
        return redirect('/lists/')
    return render(request, template_name, {'object':lista})

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
