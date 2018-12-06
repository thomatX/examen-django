from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('login/iniciar/',views.login_iniciar,name="login_iniciar"),
    path('register/',views.register,name="register"),
    path('register/create_user/',views.create_user,name="create_user"),
    path('cerrarsesion/',views.cerrar_session,name="cerrar_session"),
    path('lists/',views.lists,name="my_lists"),
    path('lists/create/',views.create_list,name="create_list"),
    path('lists/create/new/',views.create_new_list,name="create_new_list"),
    path('products/',views.products,name="my_products"),
    path('products/create/',views.create_product,name="create_product"),
    path('products/create/new/',views.create_new_product,name="create_new_product"),
    path('shopping/',views.shopping,name="shopping"),
    path('profile/',views.profile,name="profile"),

]