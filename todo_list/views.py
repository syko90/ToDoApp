from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    my_name = 'Psycho'
    return render(request, 'about.html', {'my_name': my_name})


