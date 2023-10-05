from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def login (request):
	return render(request,"proyectoweb/login.html")

def home (request):
	return render(request,"proyectoweb/home.html")

def passlost(request):
	return render(request,"proyectoweb/passlost.html")

def shop(request):
	return render(request,"proyectoweb/shop.html")

def config(request):
	return render(request,"proyectoweb/config.html")

def activos(request):
	return render(request,"proyectoweb/activos.html")

def pasados(request):
	return render(request,"proyectoweb/pasados.html")

def perfil(request):
	return render(request,"proyectoweb/perfil.html")

