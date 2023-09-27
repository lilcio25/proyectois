from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from proyectoweb import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login, name ='login'),
    path('home/',views.home, name = 'home'),
    path('login/',auth_views.LogoutView.as_view(), name='login'),
]


