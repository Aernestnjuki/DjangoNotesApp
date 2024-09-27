from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'My Notes App'
    }
    return render(request, 'index.html', context)
