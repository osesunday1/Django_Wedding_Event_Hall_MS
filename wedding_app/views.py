from django.shortcuts import render
from django.http import HttpResponse



context_dictionary = {'cars': 'Ford, Ferrari, Mustang, Range Rover, Tesla'}



def home(request):
    return render(request, 'wedding/home.html', context_dictionary )

