from django.shortcuts import render


def home(request):
    return render(request, 'version_control/home.html')

