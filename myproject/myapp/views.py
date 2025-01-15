from django.shortcuts import render

def home(request):
    context = {
        'title': 'My Blog',
        'message': 'Welcome to My Blog Homepage!',
    }
    return render(request, 'home.html', context)
