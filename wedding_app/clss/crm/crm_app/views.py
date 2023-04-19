from django.shortcuts import render




def home(request):
    context_dictionary = {'cars': 'Ford, Ferrari, Mustang, Range Rover, Tesla'}
    
    return render(request, 'crm/home.html', context_dictionary)


