# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def registro(request):
    return HttpResponse('registro.html')
