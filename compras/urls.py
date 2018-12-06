from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('login/iniciar/',views.login_iniciar,name="login_iniciar"),
    path('register/',views.register,name="register"),
    path('register/create_user/',views.create_user,name="create_user"),
    path('cerrarsesion/',views.cerrar_session,name="cerrar_session"),
    path('lists/',views.lists,name="my_lists"),
    path('lists/delete/<int:pk>/',views.delete_list,name="my_lists"),
    path('lists/create/',views.create_list,name="create_list"),
    path('lists/create/new/',views.create_new_list,name="create_new_list"),
    path('products/',views.products,name="my_products"),
    path('products/delete/<int:pk>/',views.delete_product,name="my_products"),
    path('products/create/',views.create_product,name="create_product"),
    path('products/create/new/',views.create_new_product,name="create_new_product"),
    path('shopping/',views.shopping,name="shopping"),
    path('profile/',views.profile,name="profile"),
    path('oauth/', include('social_django.urls', namespace='social')),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)