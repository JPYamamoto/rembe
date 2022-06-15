from django.shortcuts import render

def home(request):
    """View to display the template of the home."""

    return render(request, 'home/home.html')
