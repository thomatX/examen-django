from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('login/iniciar/',views.login_iniciar,name="login_iniciar"),
    path('register/',views.register,name="register"),
    path('register/create_user/',views.create_user,name="create_user"),
    path('cerrarsesion/',views.cerrar_session,name="cerrar_session"),
]