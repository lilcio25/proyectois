from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def login (request):
	return render(request,"proyectoweb/login.html")



def home (request):
	return render(request,"proyectoweb/home.html")
