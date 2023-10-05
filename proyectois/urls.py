from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from proyectoweb import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login, name ='login'),
    path('login/',auth_views.LogoutView.as_view(), name='login'),
    path('home/',views.home, name = 'home'),
    path('passlost/',views.passlost, name = 'passlost'),
    path('shop/',views.shop, name = 'shop'),
    path('activos/',views.activos, name = 'activos'),
    path('pasados/',views.pasados, name ='pasados'),
    path('config/',views.config, name ='config'),
    path('perfil/',views.perfil, name ='perfil'),


]


