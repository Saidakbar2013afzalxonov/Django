# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from . import models


def abc(request):
    users=[
        {'ism':'Saidakbar','familiya':'Avzalxonov','yosh':12},
        {'ism':'Saidansaf','familiya':'Avzalxonov','yosh':11},
    ]

    users=models.User.objects.all()
    return render(request, 'dtl.html',context={'users':users})
