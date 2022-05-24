from unicodedata import name
from django.shortcuts import render


def index(r):
    return render(r, 'main/home.html')


def about(r):
    return render(r, 'main/about.html')
